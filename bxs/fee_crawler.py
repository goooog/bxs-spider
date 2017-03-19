#!/usr/bin/env python
# -*- coding:utf-8 -*-

from settings import *
from tools import *
import json
import requests
import copy

class FeeCrawler(object):

	def __init__(self,common_data,ins_data):
		super.__init__(self)
		self.common_data=copy.deepcopy(common_data)
		self.ins_data=copy.deepcopy(ins_data)

	def run(self):
		page_id=self.submit_planbook()
		page_content=self.get_planbook_page(page_id)
		self.parse_page(page_content)
	
	def generate_params(self):
		params=self.ins_data
		params['commonData']=self.common_data
		params['insureList']=[]
		if not params.has_key('allMainInsData'):
			return params
			
		for (ins_type,ins_data) in params['allMainInsData'].items():
			if not ins_data.has_key('baoType'):
				continue

			baoType=ins_data['baoType']

			for (code,ins) in ins_data.items():
				if(ins.has_key('baoe') and ins.has_key('baof')):
					ins['code']=code
					ins['type']=ins_type
					ins['baoType']=baoType
					params['insureList'].append(ins)
		return params

			
	def submit_planbook(self):
		pb_input=self.generate_params()
		payload=dict(combinePBInput=json.dumps(pb_input))
		r=requests.post(CREAT_PB_URL,data=payload,cookies=COOKIES,verify=False)
		return r.json()['data']
	
	def get_planbook_page(self,page_id):
		if not page_id:
			return
		r=requests.get(CREAT_PB_URL+page_id,cookies=COOKIES)
		if is_http_ok(r):
			return r.content;

	
	def parse_page(self,page_content):
		if not page_content:
			return
	

		
