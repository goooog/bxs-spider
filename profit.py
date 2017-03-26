#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.ins_crawler import InsuranceCrawler
from bxs.logs.log import *

ins_ids=range(634,635)
for id in ins_ids:
	try:
		logging.info('Profit start:id=%s',id)
		ins_crawler=InsuranceCrawler(id)
		ins_crawler.run_profit()
	except BaseException,e:
		logging.error('Profit failed:id=%s,error=%s',id,e)
print 'finish!!!!!'
