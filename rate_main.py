#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.insurance import InsuranceCrawler
from bxs.loggings import *

#ins_crawler=InsuranceCrawler(634)
ins_ids=[562]
for id in ins_ids:
	try:
		logging.info('Start:id=%s',id)
		ins_crawler=InsuranceCrawler(id)
		ins_crawler.run()
	except BaseException,e:
		logging.error('Failed:id=%s,error=%s',id,e)

logging.info('Rate crawl finish!!!')
