# -*- coding: iso-8859-15 -*
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import (
    PLATFORM_SCHEMA)
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
import json
import os
import requests
import time

SCAN_INTERVAL = timedelta(minutes=5)

CONF_SELECIONAR = 'selecionar'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_SELECIONAR, default='ambos'): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    escolha = config[CONF_SELECIONAR]

    if 'metro' in escolha:
        add_devices([linha1(), linha2(), linha3(), linha4(), linha5(), linha15()], True)

    elif 'cptm' in escolha:
        add_devices([linha7(), linha8(), linha9(), linha10(), linha11(), linha12(), linha13()], True)

    elif 'ambos' in escolha:
        add_devices([linha1(), linha2(), linha3(), linha4(), linha5(), linha15(), linha7(), linha8(), linha9(), linha10(), linha11(), linha12(), linha13()], True)


class linha1(Entity):
        
    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Linha 1 - Azul"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)
        
        comecolinha1 = html.find('1b848518-57ba-4659-93bb-aff76790e352')
        finallinha1 = html.find('"codigo" : "1"}')
        
        iniciolinha1 = (comecolinha1 - 11)
        fimlinha1 = (finallinha1 + 16)

        linha1 = html[iniciolinha1:fimlinha1]
        
        linha1json = json.loads(linha1)
        aux1 = linha1json["linha"]
        
        if 'Linha 1' in aux1:
            status1 = linha1json["msgStatus"]
            if 'Normal' in status1:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status1:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status1:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status1:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha2(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 2 - Verde'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)

        comecolinha2 = html.find('02552784-b493-4a45-8abb-b8c81cea333d')
        finallinha2 = html.find('"codigo" : "2"}')

        iniciolinha2 = (comecolinha2 - 11)
        fimlinha2 = (finallinha2 + 16)

        linha2 = html[iniciolinha2:fimlinha2]

        linha2json = json.loads(linha2)
        aux2 = linha2json["linha"]

        if 'Linha 2' in aux2:
            status2 = linha2json["msgStatus"]
            if 'Normal' in status2:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status2:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status2:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status2:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"
					
class linha3(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 3 - Vermelha'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)

        comecolinha3 = html.find('307a9513-4419-49c7-8332-d7c408874e65')
        finallinha3 = html.find('"codigo" : "3"}')

        iniciolinha3 = (comecolinha3 - 11)
        fimlinha3 = (finallinha3 + 16)

        linha3 = html[iniciolinha3:fimlinha3]

        linha3json = json.loads(linha3)
        aux3 = linha3json["linha"]

        if 'Linha 3' in aux3:
            status3 = linha3json["msgStatus"]
            if 'Normal' in status3:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status3:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status3:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status3:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"
		
class linha4(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 4 - Amarela'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)

        comecolinha4 = html.find('5f75b49e-58b8-4f38-86c1-0bd33c61f785')
        finallinha4 = html.find('"codigo" : "4"}')

        iniciolinha4 = (comecolinha4 - 11)
        fimlinha4 = (finallinha4 + 16)

        linha4 = html[iniciolinha4:fimlinha4]

        linha4json = json.loads(linha4)
        aux4 = linha4json["linha"]

        if 'Linha 4' in aux4:
            status4 = linha4json["msgStatus"]
            if 'Normal' in status4:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status4:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status4:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status4:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha5(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 5 - Lilas'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)

        comecolinha5 = html.find('1875e28b-4cb0-4bac-b250-d8c74a47af4d')
        finallinha5 = html.find('"codigo" : "5"}')

        iniciolinha5 = (comecolinha5 - 11)
        fimlinha5 = (finallinha5 + 16)

        linha5 = html[iniciolinha5:fimlinha5]

        linha5json = json.loads(linha5)
        aux5 = linha5json["linha"]

        if 'Linha 5' in aux5:
            status5 = linha5json["msgStatus"]
            if 'Normal' in status5:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status5:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status5:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status5:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"
				
class linha15(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 15 - Prata'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
        http = r.text
        html = str(http)

        comecolinha15 = html.find('f46383ab-6389-411f-9193-81e46eee66dc')
        finallinha15 = html.find('"codigo" : "15"}')

        iniciolinha15 = (comecolinha15 - 11)
        fimlinha15 = (finallinha15 + 17)

        linha15 = html[iniciolinha15:fimlinha15]

        linha15json = json.loads(linha15)
        aux15 = linha15json["linha"]

        if 'Linha 15' in aux15:
            status15 = linha15json["msgStatus"]
            if 'Normal' in status15:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'Reduzida' in status15:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'Paralisada' in status15:
                self._state = "Paralisada"
                self._icon = "mdi:subway-alert-variant"
            if 'Encerrada' in status15:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha7(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 7 - Rubi'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        comecolinha7 = html.find('col-xs-4 col-sm-4 col-md-2 rubi')
        finallinha7 = html.find("/div")
        linha7 = str(html[(comecolinha7 - 12):(finallinha7 + 5)])

        if 'rubi' in linha7:
            if 'status_normal' in linha7:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha7:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha7:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha7:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha8(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 8 - Diamante'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        comecolinha8 = html.find('col-xs-4 col-sm-4 col-md-2 diamante')
        finallinha8 = html.find('/div', (finallinha7 + 5), fim)
        linha8 = html[(comecolinha8 - 12):(finallinha8 + 5)]

        if 'diamante' in linha8:
            if 'status_normal' in linha8:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha8:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha8:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha8:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha9(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 9 - Esmeralda'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        finallinha8 = html.find('/div', (finallinha7 + 5), fim)

        comecolinha9 = html.find('col-xs-4 col-sm-4 col-md-2 esmeralda')
        finallinha9 = html.find('/div', (finallinha8 + 5), fim)
        linha9 = html[(comecolinha9 - 12):(finallinha9 + 5)]

        if 'esmeralda' in linha9:
            if 'status_normal' in linha9:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha9:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha9:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha9:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha10(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 10 - Turquesa'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        finallinha8 = html.find('/div', (finallinha7 + 5), fim)

        finallinha9 = html.find('/div', (finallinha8 + 5), fim)

        comecolinha10 = html.find('col-xs-4 col-sm-4 col-md-2 turquesa')
        finallinha10 = html.find('/div', (finallinha9 + 5), fim)
        linha10 = html[(comecolinha10 - 12):(finallinha10 + 5)]

        if 'turquesa' in linha10:
            if 'status_normal' in linha10:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha10:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha10:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha10:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha11(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 11 - Coral'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        finallinha8 = html.find('/div', (finallinha7 + 5), fim)

        finallinha9 = html.find('/div', (finallinha8 + 5), fim)

        finallinha10 = html.find('/div', (finallinha9 + 5), fim)

        comecolinha11 = html.find('col-xs-4 col-sm-4 col-md-2 coral')
        finallinha11 = html.find('/div', (finallinha10 + 5), fim)
        linha11 = html[(comecolinha11 - 12):(finallinha11 + 5)]

        if 'coral' in linha11:
            if 'status_normal' in linha11:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha11:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha11:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha11:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha12(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 12 - Safira'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        finallinha8 = html.find('/div', (finallinha7 + 5), fim)

        finallinha9 = html.find('/div', (finallinha8 + 5), fim)

        finallinha10 = html.find('/div', (finallinha9 + 5), fim)

        finallinha11 = html.find('/div', (finallinha10 + 5), fim)

        comecolinha12 = html.find('col-xs-4 col-sm-4 col-md-2 safira')
        finallinha12 = html.find('/div', (finallinha11 + 5), fim)
        linha12 = html[(comecolinha12 - 12):(finallinha12 + 5)]

        if 'safira' in linha12:
            if 'status_normal' in linha12:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha12:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha12:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha12:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"

class linha13(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 13 - Jade'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property	
    def icon(self):
        return self._icon

    def update(self):
        r = requests.get("http://www.cptm.sp.gov.br/Pages/Home.aspx")
        http = r.text
        html = str(http.encode('utf-8'))

        comeco = html.find('col-sm-12 col-md-8 situacao_linhas')
        fim = html.find('ultima_atualizacao')
        html = html[(comeco + 148):(fim - 12)]

        finallinha7 = html.find("/div")

        finallinha8 = html.find('/div', (finallinha7 + 5), fim)

        finallinha9 = html.find('/div', (finallinha8 + 5), fim)

        finallinha10 = html.find('/div', (finallinha9 + 5), fim)

        finallinha11 = html.find('/div', (finallinha10 + 5), fim)

        finallinha12 = html.find('/div', (finallinha11 + 5), fim)

        comecolinha13 = html.find('col-xs-4 col-sm-4 col-md-2 jade')
        finallinha13 = html.find('/div', (finallinha12 + 5), fim)
        linha13 = html[(comecolinha13 - 12):(finallinha13 + 5)]

        if 'jade' in linha13:
            if 'status_normal' in linha13:
                self._state = "Normal"
                self._icon = "mdi:subway-variant"
            if 'status_reduzida' in linha13:
                self._state = "Velocidade Reduzida"
                self._icon = "mdi:subway-alert-variant"
            if 'status_parcial' in linha13:
                self._state = "Parcial"
                self._icon = "mdi:subway-alert-variant"
            if 'status_encerradas' in linha13:
                self._state = "Fechado"
                self._icon = "mdi:subway-alert-variant"
