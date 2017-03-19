#/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import time
import codecs
from settings import *

def write_file(text):
	with codecs.open('./product.txt','a','utf-8') as f:
		f.write(text+'\n')

for id in range(460,2000):
	common_data=dict(commonData=COMMON_DATA,insuranceTypeId=id)
	payload=dict(combinePBInput=json.dumps(common_data),callMethod=1,quickResult='true')
	try:
		resp=requests.post(GET_PB_URL,data=payload,cookies=COOKIES,verify=False)
		resp.encoding='utf-8'
		if resp.status_code==requests.codes.ok:
			data=resp.json()['data']
			if not data.has_key('retcode'):
				write_file(json.dumps(data,ensure_ascii=False))
	except BaseException, e:
	   print e
	finally:
	   time.sleep(1)



