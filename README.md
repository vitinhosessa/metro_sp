# Metro e CPTM São Paulo

Read this in [English](README-en.md).

Os dados das linhas 1 (Azul), 2 (Verde), 3 (Vermelha), 4 (Amarela), 5 (Lilas) e 15 (Prata) do Metro de São Paulo são tirados do site do [Metro](http://www.metro.sp.gov.br/).

Os dados das linhas 7 (Rubi), 8 (Diamante), 9 (Esmeralda), 10 (Turquesa), 11 (Coral), 12 (Safira) e 13 (Jade) da CPTM de São Paulo são tirados do site da [CPTM](https://www.cptm.sp.gov.br/Pages/Home.aspx).

O custom_component pode criar até 13 sensores: 
* sensor.linha_1_azul
* sensor.linha_2_verde
* sensor.linha_3_vermelha
* sensor.linha_4_amarela
* sensor.linha_5_lilas
* sensor.linha_15_prata
* sensor.linha_7_rubi
* sensor.linha_8_diamante
* sensor.linha_9_esmeralda
* sensor.linha_10_turquesa
* sensor.linha_11_coral
* sensor.linha_12_safira
* sensor.linha_13_jade

Os 4 resultados possiveis para os sensores do Metro:
* Normal
* Velocidade Reduzida
* Paralisada
* Fechado

Os 4 resultados possiveis para os sensores da CPTM:
* Normal
* Velocidade Reduzida
* Parcial
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
    scan_interval: 180  # Opicional
    selecionar: metro # Opicional
````

Variável na Configuração:
* **scan_interval** (Opicional): O padrão é 300 (5 minutos) caso não declarar essa variavel. Você pode mudar para qualquer valor que desejar, mas tenha em mente que quanto menor o valor, mais vezes o Home Assistant vai pegar a informção no site do Metro e isso pode causar uma queda de velocidade no sistema do Home Assistant e até causar falhas. Eu acho seguro no valor minimo de 60 segundos (1 minuto).

* **selecionar** (Opicional): O padrão é ``ambos`` caso não declarar essa variavel. Você pode mudar para ``metro`` ou ``cptm``. Se você escolher ``metro``, ele só vai criar entidades das linhas do Metro, que são: 1 (Azul), 2 (Verde), 3 (Vermelha), 4 (Amarela), 5 (Lilas) e 15 (Prata). Se você escolher ``cptm``, ele só vai criar entidades das linhas da CPTM, que são: 7 (Rubi), 8 (Diamante), 9 (Esmeralda), 10 (Turquesa), 11 (Coral), 12 (Safira) e 13 (Jade).

Reinicie o Home Assistant.


***OBS: Existem esses dois jeitos de atualizar esse custom_component (``metro_sp``) diretamente no Home Assistant. Só que eles dois não podem estar instalados juntos. Escolha apenas um deles!***

## Configurar [``custom_updater``](https://github.com/custom-components/custom_updater)
Adicione no ``configuration.yaml``:
````yaml
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/vitinhosessa/metro_sp/master/custom_components.json
````
Sempre que o ``metro_sp`` for atualizado pelo ``custom_updater``, reinicie o Home Assistant.

## Configurar [HACS (Home Assistant Community Store)](https://github.com/custom-components/hacs)
Entre na aba ``Community``, depois entre na aba ``Settings`` do HACS.

Copie esse link: ``https://github.com/vitinhosessa/metro_sp``

Cole o link em ``CUSTOM INTEGRATION REPO'S`` e clique no disquete.

Agora vá na aba ``Store``, procure ``Metro``, clique em ``Manage`` e depois clique em ``Install``. Mesmo que você já tenha instalado esse custom_component antes.

Reinicie o Home Assistant.

## Exemplo Lovelace Card

<img src="/images/lovelace-card-metro-cptm.png" alt="lovelace-card-metro-cptm" width="1500px" align="center">

````yaml
type: entities
title: Metro
show_header_toggle: false
entities:
  - entity: sensor.linha_1_azul
  - entity: sensor.linha_2_verde
  - entity: sensor.linha_3_vermelha
  - entity: sensor.linha_4_amarela
  - entity: sensor.linha_5_lilas
  - entity: sensor.linha_15_prata
````

````yaml
type: entities
title: CPTM
show_header_toggle: false
entities:
  - entity: sensor.linha_7_rubi
  - entity: sensor.linha_8_diamante
  - entity: sensor.linha_9_esmeralda
  - entity: sensor.linha_10_turquesa
  - entity: sensor.linha_11_coral
  - entity: sensor.linha_12_safira
  - entity: sensor.linha_13_jade
````

## Changelog

### [0.2] - 2019-05-26
#### Adições
- Foram adicionadas as linhas 7 (Rubi), 8 (Diamante), 9 (Esmeralda), 10 (Turquesa), 11 (Coral), 12 (Safira) e 13 (Jade) da CPTM de São Paulo.
- Agora as entidades já são criadas com o icone mdi:subway-variant quando a linha está funcionando normalmente, e quando está com Velocidade Reduzida, parcial, paralisada ou fechado o icone muda para mdi:subway-alert-variant.
- Opção de escolher quais entidades vao ser criadas, as linhas do Metro ou as linhas da CPTM ou ambas.

### [0.1b4] - 2019-05-23
#### Adições
- Agora é possível colocar o custom_component no HACS (Home Assistant Community Store).

### [0.1b3] - 2019-05-21
#### Adições
- Foi adicionado uma variável na configuração ``scan_interval`` caso queria mudar a frequência das atualizações das informações das linhas.
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
