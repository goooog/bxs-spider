#/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import time
import codecs
from settings import *

def write_file(text):
	with codecs.open('./data.txt','a','utf-8') as f:
		f.write(text+'\n')

def fetch_pb(insuranceId):
	common_data=dict(commonData=COMMON_DATA,insuranceTypeId=insuranceId)
	payload=dict(combinePBInput=json.dumps(common_data),callMethod=1,quickResult='true')
	return requests.post(GET_PB_URL,data=payload,cookies=COOKIES,verify=False)

def parse_response(response):

	if response.status_code!=requests.codes.ok:
		return ''

	response.encoding='utf-8'
	data=response.json()['data']
	if not data.has_key('groupDefData'):
		return ''

	group_def_data=data['groupDefData']
	ins_attr_name=group_def_data['mainInsDataOrder'][0]
	ins_id=group_def_data['insuranceTypeId']
	ins_data=group_def_data['allMainInsData'][ins_attr_name]
	ins_name=ins_data['name']
	bao_type=ins_data['baoType']
	dynamic_props=ins_data[bao_type]
	
	ins_props=[]
	for key in sorted(dynamic_props.keys()):
		value=dynamic_props[key]
		ins_props.append('{0}={1}'.format(key,value))
	
	return '{0:<4}\t{1:<15}\t{2}'.format(ins_id,ins_name,','.join(ins_props))
	
	

for id in range(460,5000):
	try:
		r=fetch_pb(id)
		data=parse_response(r)
		if data:
			print data
			write_file(data)
	except BaseException, e:
	   print e
	finally:
	   time.sleep(1)



