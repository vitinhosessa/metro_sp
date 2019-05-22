# Metro São Paulo

Read this in [English](README-en.md).

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

Adicione no ``configuration.yaml``:
````yaml
sensor:
  - platform: metro_sp
    scan_interval: 300  # Opicional
````

Variaveis na Configuração:
* **scan_interval** (Opicional): O padrão é 300 (5 minutos) caso não declarar essa variavel. Você pode mudar para qualquer valor que desejar, mas tenha em mente que quanto menor o valor, mais vezes o Home Assistant vai pegar a informção no site do Metro e isso pode causar uma queda de velocidade no sistema do Home Assistant e até causar falhas. Eu acho seguro no valor minimo de 60 segundos (1 minuto).

Reinicie o Home Assistant.

## Configurar custom_updater
Adicione no ``configuration.yaml``:
````yaml
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/vitinhosessa/metro_sp/master/custom_components.json
````
Sempre que o ``metro_sp`` for atualizado pelo ``custom_updater``, reinicie o Home Assistant.

## Exemplo Lovelace Card

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

### [0.1b3] - 2019-05-21
#### Adições
 - Foi adicionado ``scan_interval`` caso queria mudar a frequência da atualização das informações das linhas.
#### Melhorias
- Implementado um jeito melhor para fazer o update a cada 5 min.

Agradecimentos ao chat do Home Assistant no Discord que me ajudou a fazer essa implementação

### [0.1b2] - 2019-05-19
#### Mudanças
- Informações das linhas serão atualizadas a cada 5 min.

### [0.1b1] - 2019-05-19
- Primeiro release. Espero que funcione para todos. 🎉

## Licença
Este código é de domínio público. Você pode redistribuí-lo e / ou modificá-lo sob os termos da Licença Pública Geral GNU, publicada pela Free Software Foundation. http://www.gnu.org/licenses/. Certas bibliotecas podem estar sob uma licença diferente.

<a href="https://www.buymeacoffee.com/xJ7To0LNr" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
