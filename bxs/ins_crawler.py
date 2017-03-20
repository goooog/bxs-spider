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
		result=[]
		ages=range(0,80)
		sexs=[1,2]
		for age in ages:
			for sex in sexs:
				self.default_data=self.get_default_data(age,sex)
				if isinstance(self.default_data dict):
					continue
				self.variables=self.get_input_variables()
				result+=generate_input_combination()
	
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
	
	def update_field_value(self,pb_data,field,field_value):
		common_fields=('age','sex')
		if field in common_fields:
			pb_data['commonData'][field]=field_value
		else:
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				bao_type=ins['baoType']
				ins[bao_type][field]=field_value
	
	def calcurate(self,pb_data):
		return self.http_post(CALCULATE_PB_URL,pb_data,False)

	
	def get_input_variables(self):
		variables=dict()
		return variables

	def http_post(self,url,pb_input,is_quick_result):
		pb_input_json=json.dumps(pb_input,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input,callMethod=1,quickResult='true')
		if is_quick_result:
			payload['quickResult']=True
		r=requests.post(GET_PB_URL,data=payload,cookies=COOKIES,verify=False)
		if not is_http_ok(r):
			return
		data=r.json()['data']
		return data.get('groupDefData')

	
	def get_default_data(self):
		common_data=COMMON_DATA
		common_data['insuranceTypeId']=self.insurance_id
		data=self.http_post(GET_PB_URL,common_data,True)
		return self.fix_required_fields(data)
			
	def fix_required_fields(self,pb_data):
		if isinstance(pb_data,dict):
			baofei=pb_data.get('allMainBaofTotal')
			exist_bf=False
			if isinstance(baofei,str):
				if len(str)>0 and eval(baofei)>0:
					exist_bf=True
			if isinstance(baofei,int):
				if baofei>0:
					exist_bf=True
			if not exist_bf:
				self.update_field_value(pb_data,'baoe',100000)
		return pb_data
				


			



