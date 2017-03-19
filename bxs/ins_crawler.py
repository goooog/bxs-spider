#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import codecs
import json
import requests
import copy
from settings import *
from tools import *

class InsuranceCrawler:


	def __init__(self,insurance_id):
		self.insurance_id=insurance_id
	
	def run(self):
		self.default_data=self.get_default_data()
		self.variables=self.get_input_variables()
		return generate_input_combination()
	
	def generate_input_combination(self):
		combinations=[self.default_data]
		for (field,values) in self.variables.items():
			temp=[]
			for c in combinations:
				for value in values 
					temp.append(self.create_input(c,field,value))
			combinations=temp

		return combinations

	def create_input(self,base_data,field,field_value):
		data=copy.deepcopy(base_data)
		if data.has_key(field):
			data[field]=field_value
		return self.calcurate(data)
	
	def calcurate(self,payload):
		pass

	
	def get_input_variables(self):
		variables=dict()
		variables['age']=range(0,80)
		return variables


	
	def get_default_data(self):
		common_data=COMMON_DATA
		common_data['insuranceTypeId']=self.insurance_id
		pb_input=json.dumps(common_data,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input,callMethod=1,quickResult='true')
		r=requests.post(GET_PB_URL,data=payload,cookies=COOKIES,verify=False)
		if not is_http_ok(r):
			return
		data=r.json()['data']
		if data.has_key('groupDefData'):
			ins_data=data['groupDefData']
			return self.fix_required_fields(ins_data)
			
	def fix_required_fields(self,ins_data):
		pass


			



