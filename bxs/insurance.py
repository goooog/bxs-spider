#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import codecs
import json
import requests
import copy
import pprint
import re
import logging
from settings import *
from tools import *
from variables import *
from db import InsuranceDao
from loggings import *


class InsuranceCrawler:

	def __init__(self,insurance_id):
		self.insurance_id=insurance_id
		self.insdao=InsuranceDao()
	
	
	def run(self):
		self.insdao.delete(self.insurance_id)

		inputs=self.generate_request_params()
		for data in inputs:
			resp=self.calculate(data)
			self.insdao.save_insurance('insurance_rate',resp)
	
	def generate_request_params(self):
		ret=[]
		self.default_data=self.__get_default_data()
		if not isinstance(self.default_data, dict):
			logging.warning('insurance not found:%s',self.insurance_id)
			return ret
		for sex in var_fixed_range['sex']:
			for age in var_fixed_range['age']:
				try:
					ret+=self.__generate_possible_inputs(age,sex)
				except BaseException, e:
					logging.error('generate params error:%s',e)
		return ret

									
	def __generate_possible_inputs(self,age,sex):
		combinations=[]
		options=self.__get_verify_value(age,sex)
		dynamic_ranges=self.__parse_var_range(options)
		fixed_ranges=self.__generate_fixed_var_range()
		pb_data=copy.deepcopy(self.default_data)
		self.__update_field_value(pb_data,'age',age)	
		self.__update_field_value(pb_data,'sex',sex)	
		combinations.append(pb_data)
		for(field,values) in fixed_ranges.items():
			combinations=self.__generate_input_combinations(combinations,field,values)
		logging.info('age=%s sex=%s range=%s',age,sex,json.dumps(dynamic_ranges,ensure_ascii=False))
		if isinstance(dynamic_ranges,dict):
			keys=dynamic_ranges.keys()
			if len(keys)>0:
				for key in keys:
					values=dynamic_ranges[key]
					if isinstance(values,dict):
						temp=[]
						for vk in values.keys():
							combinations=self.__generate_input_combinations(combinations,key,[vk])
							for vkk in values[vk].keys():
								vkk_values=values[vk][vkk]
								temp+=self.__generate_input_combinations(combinations,vkk,vkk_values)
						combinations=temp
					else:
						combinations=self.__generate_input_combinations(combinations,key,values)
		return combinations

	def __generate_input_combinations(self,combinations,field,values):
		if not values or len(values)==0:
			return combinations

		ret=[]
		for value in values:
			for pb in combinations:
				pb=copy.deepcopy(pb)
				self.__update_field_value(pb,field,value)
				ret.append(pb)
				
		return ret
				

	def __generate_fixed_var_range(self):
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

	def __get_verify_value(self,age,sex):
		pb_data=copy.deepcopy(self.default_data)
		self.__update_field_value(pb_data,'age',age)
		self.__update_field_value(pb_data,'sex',sex)
		
		if isinstance(pb_data,dict) and pb_data.has_key('allMainInsData'):
			ins_data=pb_data['allMainInsData']
			for (key,ins) in ins_data.items():
				if not ins.has_key('baoType'):
					continue
				bao_type=ins['baoType']
				pb_data['currActive']=key
				pb_data['callMethod']=1
				return self.get_variable_option(pb_data)

	
	def __parse_var_range(self,data):
		if not isinstance(data,dict) or not data.has_key('verifyArr'):
			return
		props=data['verifyArr']
		values=data['verifyValue']
		if len(props)>0 and not values:
			raise BaseException('get_verify_value error:variable invalid')

		ret={}
		if len(props)==1:
			ret[props[0]]=[]	
			for value in values.split(','):
				key_value=str2int(value)
				if not key_value:
					continue
				ret[props[0]].append(key_value)
		elif len(props)==2:
			if not isinstance(values,dict):
				return
			ret[props[0]]={}	
			for(key,value) in values.items():
				key_value=str2int(key)
				if not key_value:
					continue
				pair=ret[props[0]]
				pair[key_value]={}
				pair[key_value][props[1]]=[str2int(v) for v in value.split(',')]
				
		return ret
	

	def __update_field_value(self,pb_data,field,field_value):
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
		return self.__http_post(CALCULATE_PB_URL,pb_data,False)


	def __http_post(self,url,pb_input,is_quick_result=False):
		pb_input_json=json.dumps(pb_input,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input_json,callMethod=1,quickResult='true')
		if is_quick_result:
			payload['quickResult']=True
		r=http_post(url,payload)
		if not is_http_ok(r) or not r.json().has_key('data'):
			return
		data=r.json()['data']
		return data.get('groupDefData')
	

	def get_variable_option(self,pb_data):
		pb_input_json=json.dumps(pb_data,ensure_ascii=False)
		payload=dict(combinePBInput=pb_input_json)
		r=http_post(GET_VERIFY_URL,payload)
		if not is_http_ok(r):
			return
		data=r.json()['data']
		return data
		
		
	
	def __get_default_data(self,age=0,sex=1,need_fix=True):
		common_data=copy.deepcopy(COMMON_DATA)
		common_data['age']=age
		common_data['sex']=sex
		pb_data=dict()
		pb_data['insuranceTypeId']=self.insurance_id
		pb_data['commonData']=common_data
		data=self.__http_post(GET_PB_URL,pb_data,True)
		if need_fix:
			return self.__fix_required_fields(data)
		else:
			return data
			
	def __fix_baoe_field(self,pb_data):
		baofei=pb_data.get('allMainBaofTotal')
		exist_bf=False
		if isinstance(baofei,basestring):
			if len(baofei)>0 and eval(baofei)>0:
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
						self.__update_field_value(pb_data,'baoe',20000)
				elif variables.has_key('baof'):
						self.__update_field_value(pb_data,'baof',10000)
	
	def __select_required_ins(self,pb_data):
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
					 if is_required:
						 v['isChecked']=True
				elif k==bao_type:
					 v['isChecked']=True
						

	def __fix_required_fields(self,pb_data):
		if isinstance(pb_data,dict):
			self.__fix_baoe_field(pb_data)
			self.__select_required_ins(pb_data)
			pb_data=self.calculate(pb_data)
		return pb_data
				



