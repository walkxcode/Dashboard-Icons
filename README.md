> [!WARNING]
> The repository has been migrated from `walkxcode` to `homarr-labs`, because I do not have the capacity/time to keep maintaining it. The Homarr team will take over all management and maintenance, whilst keeping all functionality for you, the user, the same. The project will always be usable outside of Homarr itself and breaking changes will not be made. ^Bjorn
>
> The license and guidelines have changed, so please review them. If you want to help with maintenance, reach out to [homarr-labs@proton.me](mailto:homarr-labs@proton.me).

[![jsDelivr hits (GitHub)](https://img.shields.io/jsdelivr/gh/hy/homarr-labs/dashboard-icons?style=flat-square&color=%23A020F0)](https://www.jsdelivr.com/package/gh/homarr-labs/dashboard-icons)
[![jsDelivr hits (GitHub)](https://img.shields.io/jsdelivr/gh/hy/walkxcode/dashboard-icons?style=flat-square&color=%23A020F0)](https://www.jsdelivr.com/package/gh/walkxcode/dashboard-icons)

## Dashboard Icons

The best source for dashboard icons.<br />
[**View icons →**](ICONS.md)

## Table of Contents
- [Dashboard Icons](#dashboard-icons)
- [Table of Contents](#table-of-contents)
- [Icon Requests](#icon-requests)
- [Supported Dashboards](#supported-dashboards)
- [Usage and Details](#usage-and-details)
  - [Direct Links](#direct-links)
    - [Base URL](#base-url)
    - [Name](#name)
    - [Formats](#formats)
  - [Dark/Light Versions](#darklight-versions)
  - [Downloading Icons](#downloading-icons)
- [Disclaimer](#disclaimer)

## Icon Requests

If you're looking to add a new icon, please read the [Contribution Guidelines](CONTRIBUTING.md). Afterwards, submit a Pull Request or open an issue.

## Supported Dashboards

Several dashboards offer seamless integration with Dashboard Icons. Here are some of the most popular options:

- [Homarr](https://github.com/ajnart/homarr)
- [Homepage](https://github.com/gethomepage/homepage)
- [Dashy](https://github.com/Lissy93/dashy)

## Usage and Details

### Direct Links

Icons can be used directly from either GitHub or jsDelivr (recommended). Links consist of three components, each described below:

- **Base URL**
- **Name**
- **Format**

A complete link will look like this:

    https://<Base URL>/<Format>/<Name>.<Format>

For example, the icon URL for the WEBP version of Nextcloud Calendar would be:

    https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/webp/nextcloud-calendar.webp

#### Base URL

We recommend using jsDelivr, a free and fast CDN:

- `https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons`

Alternatively, you can use direct links to the repository:

- `https://raw.githubusercontent.com/homarr-labs/dashboard-icons/refs/heads/main`

#### Name

Icons are named using kebab case (lowercase words separated by hyphens). For example, "Nextcloud Calendar" becomes `nextcloud-calendar`.

#### Formats

Icons are available in the following formats:

- SVG
- PNG
- WEBP

All icons are generated from the SVG file as the base.

*Read more about the specifics and standards of icons in the [Contribution Guidelines](CONTRIBUTING.md).*

### Dark/Light Versions

In some cases, an icon might have very light or dark colors, making it hard to see on certain backgrounds. In this situation, a `-light` or `-dark` version will be added to the end of the icon's name, with colors adjusted accordingly.

For example, "2fauth" becomes `2fauth-light`.

*Read more about the specifics and standards of icons in the [Contribution Guidelines](CONTRIBUTING.md).*

### Downloading Icons

To download icons from the [icons page](ICONS.md), simply Right-click the icon link and select "Save link as".

**Warning**: Visiting the icons page will load every icon in the repository. This may result in:

- High data usage.
- System slowdowns.
- Browser crashes on some devices.

If you prefer not to load all icons at once, consider using the direct links or downloading icons individually.

To download icons using the terminal, use `curl` or `wget`. Refer to [Direct Links](#direct-links) for details on the link structure.

    curl -O https://<Base URL>/<Format>/<Name>.<Format>

or

    wget https://<Base URL>/<Format>/<Name>.<Format>

## Disclaimer

Unless otherwise indicated, all images and assets in this repository, including product names, trademarks, and registered trademarks, are the property of their respective owners. These images and assets are used for identification purposes only, and their use does not imply endorsement.

Read the [LICENSE](LICENSE) for more information about the project itself. For questions or concerns, contact us at [homarr-labs@proton.me](mailto:homarr-labs@proton.me).
