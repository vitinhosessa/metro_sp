# -*- coding: iso-8859-15 -*
from homeassistant.helpers.entity import Entity
import os
import json

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([linha1()], [linha2()], [linha3()], [linha4()], [linha5()], [linha15()])

class linha1(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Linha 1 - Azul'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86")
		html = str(http)
		
        comecolinha1 = html.find('1b848518-57ba-4659-93bb-aff76790e352')
		finallinha1 = html.find('"codigo" : "1"}')

		linha1 = html[(comecolinha1 - 11):(finallinha1 + 16)]
		
		linha1json = json.loads(linha1)
		aux1 = linha1json["linha"]

		if 'Linha 1' in aux1:
			status1 = linha1json["msgStatus"]
			if 'Normal' in status1:
				self._state = "Normal"
			if 'Reduzida' in status1:
				self._state = "Velocidade Reduzida"
			if 'Encerrada' in status1:
				self._state = "Fechado"
			
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

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86").read()
		html = str(http)
		
		comecolinha2 = html.find('02552784-b493-4a45-8abb-b8c81cea333d')
		finallinha2 = html.find('"codigo" : "2"}')

		linha2 = html[(comecolinha2 - 11):(finallinha2 + 16)]
		
		linha2json = json.loads(linha2)
		aux2 = linha2json["linha"]

		if 'Linha 2' in aux2:
			status2 = linha2json["msgStatus"]
				if 'Normal' in status2:
					self._state = "Normal"
				if 'Reduzida' in status2:
					self._state = "Velocidade Reduzida"
				if 'Encerrada' in status2:
					self._state = "Fechado"
					
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

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86").read()
		html = str(http)
		
		comecolinha3 = html.find('307a9513-4419-49c7-8332-d7c408874e65')
		finallinha3 = html.find('"codigo" : "3"}')

		linha3 = html[(comecolinha3 - 11):(finallinha3 + 16)]

		linha3json = json.loads(linha3)
		aux3 = linha3json["linha"]

		if 'Linha 3' in aux3:
			status3 = linha3json["msgStatus"]
			if 'Normal' in status3:
				self._state = "Normal"
			if 'Reduzida' in status3:
				self._state = "Velocidade Reduzida"
			if 'Encerrada' in status3:
                self._state = "Fechado"
		
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

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86").read()
		html = str(http)
		
		comecolinha4 = html.find('5f75b49e-58b8-4f38-86c1-0bd33c61f785')
		finallinha4 = html.find('"codigo" : "4"}')

		linha4 = html[(comecolinha4 - 11):(finallinha4 + 16)]

		inha4json = json.loads(linha4)
		aux4 = linha4json["linha"]

		if 'Linha 4' in aux4:
			status4 = linha4json["msgStatus"]
			if 'Normal' in status4:
				self._state = "Normal"
			if 'Reduzida' in status4:
                self._state = "Velocidade Reduzida"
			if 'Encerrada' in status4:
				self._state = "Fechado"

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

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86").read()
		html = str(http)
		
		comecolinha5 = html.find('1875e28b-4cb0-4bac-b250-d8c74a47af4d')
		finallinha5 = html.find('"codigo" : "5"}')

		linha5 = html[(comecolinha5 - 11):(finallinha5 + 16)]

		linha5json = json.loads(linha5)
		ux5 = linha5json["linha"]

		if 'Linha 5' in aux5:
			status5 = linha5json["msgStatus"]
			if 'Normal' in status5:
                self._state = "Normal"
			if 'Reduzida' in status5:
                self._state = "Velocidade Reduzida"
			if 'Encerrada' in status5:
                self._state = "Fechado"
				
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

    def update(self):
		http = os.popen("curl http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx?id=9798c019-a3f5-476f-8a3e-911eb63a0a86").read()
		html = str(http)
		
		comecolinha15 = html.find('f46383ab-6389-411f-9193-81e46eee66dc')
		finallinha15 = html.find('"codigo" : "15"}')

		linha15 = html[(comecolinha15 - 11):(finallinha15 + 17)]

		linha15json = json.loads(linha15)
		aux15 = linha15json["linha"]

		if 'Linha 15' in aux15:
			status15 = linha15json["msgStatus"]
			if 'Normal' in status15:
                self._state = "Normal"
			if 'Reduzida' in status15:
                self._state = "Velocidade Reduzida"
			if 'Encerrada' in status15:
                self._state = "Fechado"

			
