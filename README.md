# Metro São Paulo

Read this in [English](README.md).

Os dados das linhas 1 (Azul), 2 (Verde), 3 (Vermelha), 4 (Amarela), 5 (Lilas) e 15 (Prata) do Metro de São Paulo são tirados do site do [Metro](http://www.metro.sp.gov.br/).

O custom_component cria 6 sensores: 
* sensor.linha_1_azul
* sensor.linha_2_verde
* sensor.linha_3_vermelha
* sensor.linha_4_amarela
* sensor.linha_5_lilas
* sensor.linha_15_prata

Os 3 possiveis resultados:
* Normal
* Velocidade Reduzida
* Fechado

## Instalação
Baixe nos releases o arquivo .zip ([aqui](https://github.com/vitinhosessa/metro_sp/releases)) e a copie a pasta ``metro_sp`` para ``config/custom_components/`` , onde os arquivos ficariam assim:
* ``config/custom_components/metro_sp/__init__.py``
* ``config/custom_components/metro_sp/device_tracker.py``
* ``config/custom_components/metro_sp/manifest.json``

## Exemplo Lovelace Card

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

## Licença
Este código é de domínio público. Você pode redistribuí-lo e / ou modificá-lo sob os termos da Licença Pública Geral GNU, publicada pela Free Software Foundation. http://www.gnu.org/licenses/. Certas bibliotecas podem estar sob uma licença diferente.
