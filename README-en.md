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
````

## Config custom_updater
Add to ``configuration.yaml``:
````yaml
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/vitinhosessa/metro_sp/master/custom_components.json
````
Whenever ``metro_sp`` is updated by `` custom_updater``, restart your Home Assistant.

## Lovelace Card Example

<img src="/images/lovelace-card-metro.png" alt="lovelace-card-metro" width="500px" align="center">

````yaml
type: entities
title: Metro
show_header_toggle: false
entities:
  - entity: sensor.linha_1_azul
    name: Linha 1 - Azul
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_2_verde
    name: Linha 2 - Verde
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_3_vermelha
    name: Linha 3 - Vermelha
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_4_amarela
    name: Linha 4 - Amarela
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_5_lilas
    name: Linha 5 - Lilas
    icon: 'mdi:subway-variant'
  - entity: sensor.linha_15_prata
    name: Linha 15 - Prata
    icon: 'mdi:subway-variant'
````

## Changelog

### [0.1b2] - 2019-05-19
#### Changed
- Lines informations will be checked every 5 min.

### [0.1b1] - 2019-05-19
- First release.

## License
This code is public domain. You can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. http://www.gnu.org/licenses/. Certain libraries used may be under a different license.

<a href="https://www.buymeacoffee.com/xJ7To0LNr" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
