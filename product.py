#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import json
import codecs
from bxs.ins_crawler import InsuranceCrawler

def write_file(text):
	with codecs.open('./data.txt','a','utf-8') as f:
		f.write(text+'\n')

for id in range(607,815):
	print id
	ins_crawler=InsuranceCrawler(id)
	data=ins_crawler.get_default_data(1,1,False)
	if isinstance(data,dict) and data.has_key('allMainInsData'):
		ins_data=data['allMainInsData']
		for (key,ins) in ins_data.items():
			if not ins.has_key('baoType'):
				continue
			bao_type=ins['baoType']
			name=ins['name']

			data['currActive']=key
			data['callMethod']=1
			options=ins_crawler.get_variable_option(data)

			variables=ins[bao_type]
			keys=variables.keys()
			keys.sort()
			output=''
			for v in keys:
				output+='{0}={1},'.format(v,variables[v])
			write_file("{0:<5}\t{1:<20}\t{2:<80}\t{3}".format(id,name,output.rstrip(','),json.dumps(options,ensure_ascii=False)))
