#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import codecs
import json
import requests
import copy
import pprint
from settings import *
from tools import *

class InsuranceCrawler:

	def __init__(self,insurance_id):
		self.insurance_id=insurance_id
	
	def run(self):
		result=[]
		ages=range(0,2)
		sexs=[1,2]

		for age in ages:
			for sex in sexs:
				self.default_data=self.get_default_data(age,sex)
				if not isinstance(self.default_data, dict):
					continue
				self.variables=self.get_input_variables()
				result+=self.generate_input_combination()

		return result
	
	def generate_input_combination(self):
		combinations=[self.default_data]
		for (field,values) in self.variables.items():
			temp=[]
			for c in combinations:
				for value in values:
					temp.append(self.calc_pb_data(c,field,value))
			combinations=temp

		return combinations

	def calc_pb_data(self,base_data,field,field_value):
		pb_data=copy.deepcopy(base_data)
		self.update_field_value(pb_data,field,field_value)
		return self.calculate(data)
	
	def update_field_value(self,pb_data,field,field_value):
		common_fields=('age','sex')
		if field in common_fields:
			pb_data['commonData'][field]=field_value
		else:
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				bao_type=ins['baoType']
				ins[bao_type][field]=field_value
	
	def calculate(self,pb_data):
		return self.http_post(CALCULATE_PB_URL,pb_data,False)

	
	def get_input_variables(self):
		variables=dict()
		return variables

	def http_post(self,url,pb_input,is_quick_result=False):
		pb_input_json=json.dumps(pb_input,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input_json,callMethod=1,quickResult='true')
		if is_quick_result:
			payload['quickResult']=True
		r=requests.post(url,data=payload,cookies=COOKIES,verify=False)
		if not is_http_ok(r) or not r.json().has_key('data'):
			return
		data=r.json()['data']
		return data.get('groupDefData')
		

	def get_variable_option(self,pb_data):
		pb_input_json=json.dumps(pb_data,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input_json)
		r=requests.post(GET_VERIFY_URL,data=payload,cookies=COOKIES,verify=False)
		if not is_http_ok(r):
			return
		data=r.json()['data']
		return data
		
		
	
	def get_default_data(self,age,sex,need_fix=True):
		common_data=copy.deepcopy(COMMON_DATA)
		common_data['age']=age
		common_data['sex']=sex
		pb_data=dict()
		pb_data['insuranceTypeId']=self.insurance_id
		pb_data['commonData']=common_data
		data=self.http_post(GET_PB_URL,pb_data,True)
		if need_fix:
			return self.fix_required_fields(data)
		else:
			return data
			
	def fix_baoe_field(self,pb_data):
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
	
	def select_required_ins(self,pb_data):
		ins_data=pb_data['allMainInsData']
		for (key,ins) in ins_data.items():
			if not isinstance(ins,dict) or not ins.has_key('baoType'):
				continue
			bao_type=ins['baoType']
			ins['hadChoice']=True
			for(k,v) in ins.items():
				if not isinstance(v,dict) or not v.has_key('code'):
					continue
				is_required=v.get('isRequired')
				if isinstance(is_required,bool):
					 v['isChecked']=is_required
				elif k==bao_type:
					 v['isChecked']=True
				else:
					 v['isChecked']=False
						

	def fix_required_fields(self,pb_data):
		if isinstance(pb_data,dict):
			self.fix_baoe_field(pb_data)
			self.select_required_ins(pb_data)
			pb_data=self.calculate(pb_data)
		return pb_data
				

if __name__ == '__main__':
	ins_crawler=InsuranceCrawler(3453)
	pprint.pprint(ins_crawler.run())
			



