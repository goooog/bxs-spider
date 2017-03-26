#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.ins_crawler import InsuranceCrawler
from bxs.logs.log import *

#ins_crawler=InsuranceCrawler(634)
ins_ids=[562]+range(568,812)+range(3067,4000)
for id in ins_ids:
	try:
		logging.info('Start:id=%s',id)
		ins_crawler=InsuranceCrawler(id)
		ins_crawler.run_fee()
	except BaseException,e:
		logging.error('Failed:id=%s,error=%s',id,e)
print 'finish!!!!!'
