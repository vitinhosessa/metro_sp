# São Paulo Subway

Leia isso em [Brazillian Portuguese](README.md).

The data of the lines 1 (Blue), 2 (Green), 3 (Red), 4 (Yellow), 5 (Purple) and 15 (Silver) of the São Paulo's subway are taken from [Metro](http://www.metro.sp.gov.br/).

The custom_component creates 6 sensors:
* sensor.linha_1_azul
* sensor.linha_2_verde
* sensor.linha_3_vermelha
* sensor.linha_4_amarela
* sensor.linha_5_lilas
* sensor.linha_15_prata

The 3 possible results:
* Normal (Normal)
* Velocidade Reduzida (Reduced Speed)
* Fechado (Closed)

## Installation
Download the .zip file ([here](https://github.com/vitinhosessa/metro_sp/releases)) and copy the folder `` metro_sp`` and paste on ``config/custom_components/``, where the files would look like this:
* ``config/custom_components/metro_sp/__init__.py``
* ``config/custom_components/metro_sp/device_tracker.py``
* ``config/custom_components/metro_sp/manifest.json``

Add to ``configuration.yaml``:
````yaml
sensor:
  - platform: metro_sp
    scan_interval: 300  # Optional
````

Configuration variable:
* **scan_interval** (Optional): The default is value is 300 (5 minutes) if you don't want to declare this variable. You can change to any value you want but keep in mind that the lowest value will make more updates, and will pick up an information on the Subway website and may have a speed drop on the Home Assist system and a maybe a crash. I think the lowest safest value is 60 seconds (1 minute).

Restart your Home Assistant.


***PS: There are two ways to update this custom_component (`` metro_sp``) directly in the Home Assistant. Except that the two of them can not be installed together. Choose only one of them!***

## Config [``custom_updater``](https://github.com/custom-components/custom_updater)
Add to ``configuration.yaml``:
````yaml
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/vitinhosessa/metro_sp/master/custom_components.json
````
Whenever ``metro_sp`` is updated by `` custom_updater``, restart your Home Assistant.

## Config [HACS (Home Assistant Community Store)](https://github.com/custom-components/hacs)
Go to ``Community`` tab, then go to ``Settings`` tab on HACS.

Copy this link: ``https://github.com/vitinhosessa/metro_sp``

Paste this link into ``CUSTOM INTEGRATION REPO'S`` and click on the floppy disk.

Now go to ``Store`` tab, search ``Metro``, click on ``Manage`` and click on ``Install``. Even if you have already installed this custom_component before.

Restart your Home Assistant.

## Lovelace Card Example

<img src="/images/lovelace-card-metro.png" alt="lovelace-card-metro" width="500px" align="center">

````yaml
type: entities
title: Metro
show_header_toggle: false
entities:
  - entity: sensor.linha_1_azul
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_2_verde
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_3_vermelha
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_4_amarela
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_5_lilas
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_15_prata
    icon: 'mdi:subway-variant'
````

## Changelog

### [0.1b4] - 2019-05-23
#### Adições
- Now it's possible to add the custom_component on HACS (Home Assistant Community Store).

### [0.1b3] - 2019-05-21
#### New
 - Added the configuration variable "scan_interval" to change the update rate to get the line information.
#### Improvement
- A better way to do the update every 5 minutes was implemented.

Thanks to the Home Assistant chat on Discord that helped me make this implementation.

### [0.1b2] - 2019-05-19
#### Changed
- Lines informations will be checked every 5 min.

### [0.1b1] - 2019-05-19
- First release.

## License
This code is public domain. You can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. http://www.gnu.org/licenses/. Certain libraries used may be under a different license.

<a href="https://www.buymeacoffee.com/xJ7To0LNr" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
