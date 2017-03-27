#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.profit import ProfitCrawler
from bxs.loggings import *

ins_ids=range(546,547)
for id in ins_ids:
	try:
		logging.info('Profit start:id=%s',id)
		profit_crawler=ProfitCrawler(id)
		profit_crawler.run()
	except BaseException,e:
		logging.error('Profit failed:id=%s,error=%s',id,e)
	
logging.info("Profit crawler finish")
