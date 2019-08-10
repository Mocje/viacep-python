#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from sys import exit

__version__ = '1.3.1'

class ViaCEP:
	self.sit = None

	#def __init__(self, cep):
	#	self.cep = cep

	def getDadosCEP(self, cep):
		self.cep = cep
		url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
		req = requests.get(url_api)
		if req.status_code == 200:
			dados_json = json.loads(req.text)
			self.sit = dados_json
		elif req.status_code == 404:
			self.sit = {'error': True, '__cause__': 'Not Found', 'error_code': 404}
			
		else:
			self.sit = {'error': True, '__cause__': 'Forbidden' 'error_code': 402}
			
		return self.sit
