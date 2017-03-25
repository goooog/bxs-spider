#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import codecs
import json
import requests
import copy
import pprint
import re
from settings import *
from tools import *
from variables import *

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
	
	def run_fee(self):
		self.default_data=self.get_default_data()
		if not isinstance(self.default_data, dict):
			print 'insurance not found',self.insurance_id
			return
		inputs=[]
		for sex in var_fixed_range['sex']:
			for age in var_fixed_range['age']:
				try:
					inputs+=self.generate_possible_inputs(age,sex)
				except BaseException, e:
					pass
		for data in inputs:
			resp=self.calculate(data)
			self.print_fee_rate(resp)
			
	def print_fee_rate(self,resp):
		print json.dumps(resp,ensure_ascii=False)

			
									
	def generate_possible_inputs(self,age,sex):
		combinations=[]
		options=self.get_verify_value(age,sex)
		dynamic_ranges=self.parse_var_range(options)
		fixed_ranges=self.generate_fixed_var_range()
		pb_data=copy.deepcopy(self.default_data)
		self.update_field_value(pb_data,'age',age)	
		self.update_field_value(pb_data,'sex',sex)	
		combinations.append(pb_data)
		for(field,values) in fixed_ranges.items():
			combinations=self.generate_input_combinations(combinations,field,values)
		if isinstance(dynamic_ranges,dict):
			keys=dynamic_ranges.keys()
			if len(keys)>0:
				for key in keys:
					values=dynamic_ranges[key]
					if isinstance(values,dict):
						for vk in values.keys():
							combinations=self.generate_input_combinations(combinations,key,vk)
							for vkk in values[vk].keys():
								vkk_values=values[vk][vkk]
								for vkk_value in vkk_values:
									combinations=self.generate_input_combinations(combinations,vkk,vkk_value)
					else:
						for value in values:
							combinations=self.generate_input_combinations(combinations,key,value)
		return combinations

	def generate_input_combinations(self,combinations,field,values):
		if not values or len(values)==0:
			return combinations

		ret=[]
		for value in values:
			for pb in combinations:
				pb=copy.deepcopy(pb)
				self.update_field_value(pb,field,value)
				ret.append(pb)
				
		return ret
				

	def generate_fixed_var_range(self):
		pb_data=self.default_data
		ins_data=pb_data['allMainInsData']
		ret={}
		for (key,ins) in ins_data.items():
			if not isinstance(ins,dict) or not ins.has_key('baoType'):
				continue
			bao_type=ins['baoType']
			ins_vars=ins[bao_type]
			if not isinstance(ins_vars,dict):
				continue
			for key in ins_vars.keys():
				if key in var_fixed_range:
					values=var_fixed_range[key]
					ret[key]=values
		return ret

	def get_verify_value(self,age,sex):
		pb_data=copy.deepcopy(self.default_data)
		self.update_field_value(pb_data,'age',age)
		self.update_field_value(pb_data,'sex',sex)
		
		if isinstance(pb_data,dict) and pb_data.has_key('allMainInsData'):
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				if not ins.has_key('baoType'):
					continue
				bao_type=ins['baoType']
				pb_data['currActive']=key
				pb_data['callMethod']=1
				return self.get_variable_option(pb_data)

	
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
	
	def parse_var_range(self,data):
		if not isinstance(data,dict) or not data.has_key('verifyArr'):
			return
		props=data['verifyArr']
		values=data['verifyValue']
		if len(props)>0 and not values:
			raise BaseException('invalid input')

		ret={}
		if len(props)==1:
			ret[props[0]]=[]	
			for value in values.split(','):
				ret[props[0]].append(self.parse_var_value(value))
		elif len(props)==2:
			if not isinstance(values,dict):
				return
			ret[props[0]]={}	
			for(key,value) in values.items():
				key_value=self.parse_var_value(key)
				if not key_value:
					continue
				pair=ret[props[0]]
				pair[key_value]={}
				pair[key_value][props[1]]=value.split(',')
				
		return ret
	
	def parse_var_value(self,value):
		if value=='趸交':
			return 1
		elif value=='终身':
			return 100
		match=re.match(r'.*?(\d+).*',value)
		if match:
			return match.group(1)
		else:
			print 'not matched:'+value


	def update_field_value(self,pb_data,field,field_value):
		common_fields=('age','sex')
		if field in common_fields:
			pb_data['commonData'][field]=field_value
		else:
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				bao_type=ins['baoType']
				target=ins[bao_type]
				target[field]=field_value
				if field=='baoe' and target.has_key('baofToBaoe'):
					target['baofToBaoe']=0
				elif field=='baof' and target.has_key('baofToBaoe'):
					target['baofToBaoe']=1
	
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
		
		
	
	def get_default_data(self,age=0,sex=1,need_fix=True):
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
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				bao_type=ins['baoType']
				variables=ins[bao_type]
				if variables.has_key('baoe'):
					baoe='{0}'.format(variables['baoe'])
					if baoe!='-':
						self.update_field_value(pb_data,'baoe',200000)
				elif variables.has_key('baof'):
						self.update_field_value(pb_data,'baof',10000)
	
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
			



