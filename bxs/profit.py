#!/usr/bin/env python
# -*- coding:utf-8 -*-

from settings import *
from tools import *
import json
import requests
import copy
import logging

from loggings import *
from bs4 import BeautifulSoup
from insurance import InsuranceCrawler
from db import ProfitDao,InsuranceDao

class ProfitCrawler(object):

	def __init__(self,insurance_id):
		self.insurance_id=insurance_id
		self.inscrawler=InsuranceCrawler(insurance_id)
		self.profitdao=ProfitDao()
		self.insdao=InsuranceDao()


	def run(self):
		self.profitdao.delete_profits(self.insurance_id)
		params=self.inscrawler.generate_request_params()
		for param in params:
			param=self.inscrawler.calculate(param)
			data=self.__crawl_profits(param)
			profit_id=self.insdao.save_insurance('insurance_profit_variable',param)
			self.profitdao.save_profits(data,profit_id,self.insurance_id)
	
	def __crawl_profits(self,params):
		page_id=self.__submit_planbook(params)
		page_content=self.__get_planbook_page(page_id)
		data=self.__parse_planbook_page(page_content)
		return data
	
	def __rebuild_params(self,params):
		params['insureList']=[]
		if not params.has_key('allMainInsData'):
			return params
			
		for (ins_type,ins_data) in params['allMainInsData'].items():
			if not ins_data.has_key('baoType'):
				continue

			baoType=ins_data['baoType']

			for (code,ins) in ins_data.items():
				if not isinstance(ins,dict):
					continue

				if ins.has_key('baoe') and ins.has_key('baof'):
					ins['code']=code
					ins['type']=ins_type
					ins['baoType']=baoType
					params['insureList'].append(ins)
		return params

			
	def __submit_planbook(self,params):
		pb_input=self.__rebuild_params(params)
		payload=dict(combinePBInput=json.dumps(pb_input,ensure_ascii=False))
		r=http_post(CREAT_PB_URL,payload)
		if is_http_ok(r):
			return r.json()['data']
	
	def __get_planbook_page(self,page_id):
		if not page_id:
			return
		r=http_get(PB_PAGE_URL+page_id)
		if is_http_ok(r):
			return r.text

	
	def __parse_planbook_page(self,page_content):
		if not page_content:
			return
		soup=BeautifulSoup(page_content)
		scripts=soup.find_all('script')
		data=''
		for script in scripts:
			if not script.string:
				continue
			s=script.string.strip()
			if s.startswith('var data'):
				data=s.split('\n')[0].rstrip(';')
				start=data.index('{')
				data=data[start:]

		if data:
			return json.loads(data)
				

		
