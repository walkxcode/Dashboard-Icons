import os
import json
import sys
import base64
from pathlib import Path
import re

def generate_folder_tree(paths):
    tree = {}
    webp_files = []
    for path in paths:
        resolved_path = Path(path).resolve()
        base_folder = resolved_path.name or Path.cwd().name
        for root, _, files in os.walk(resolved_path):
            relative_path = os.path.relpath(root, resolved_path)
            key = base_folder if relative_path == '.' else os.path.join(base_folder, relative_path)
            if files:
                tree[key] = sorted(files)  # Sort the list of files alphabetically
                # Collect WebP files for XML generation
                for file in files:
                    if file.lower().endswith('.webp'):
                        webp_files.append(os.path.join(root, file))
    return tree, webp_files

def generate_webp_xml(webp_files):
    json_obj_list = []
    for path in webp_files:
        with open(path, "rb") as image_file:
            # Encode the WebP image to base64
            data = base64.b64encode(image_file.read()).decode('ascii')

            # Build the base64 string for data URI
            data_string = f"data:image/webp;base64,{data}"

            # Extract name from the path
            name = Path(path).stem

            # Append the base64 encoded WebP data into the list
            json_obj_list.append({
                "data": data_string,
                "w": 48,
                "h": 48,
                "title": name,
                "aspect": "fixed"
            })

    # Convert to JSON string with no extra spaces for XML output
    return json.dumps(json_obj_list, separators=(',', ':'))

if __name__ == "__main__":
    # Adjust paths to be one level up
    folder_paths = sys.argv[1:]
    folder_paths = [str(Path(path).resolve()) for path in folder_paths]

    if not folder_paths:
        print("Please provide at least one folder path.")
        sys.exit(1)

    # Generate the folder tree and get WebP files
    folder_tree, webp_files = generate_folder_tree(folder_paths)

    # Write the JSON structure to 'tree.json' in the parent folder
    root_dir = Path(__file__).resolve().parent
    tree_json_path = root_dir.parent / 'tree.json'
    with open(tree_json_path, 'w') as f:
        json.dump(folder_tree, f, indent=4, sort_keys=True)  # Sort the keys in the JSON output
    print(f"Folder tree successfully written to '{tree_json_path}'.")

    # Generate WebP XML
    if webp_files:
        webp_json = generate_webp_xml(webp_files)

        # Write XML structure (with wrapped JSON) to 'tree.xml'
        xml_output_path = root_dir.parent / 'tree.xml'
        with open(xml_output_path, 'w') as xml_output:
            print(f"<mxlibrary>{webp_json}</mxlibrary>", file=xml_output)
        print(f"WebP assets successfully written to '{xml_output_path}'.")
    else:
        print("No WebP files found for XML generation.")