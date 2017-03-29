#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.insurance import InsuranceCrawler
from bxs.loggings import *

#ins_ids=[3324,588,644,789,457,460,452,78,3451,3453,559,3188,3276,451,610,445,319,320,3233,388,3109,3122,496,774,488,3362,24,413,619]
ins_ids=[3324,588,457,460,78,3451,3453,559,3188,3276,451,445,319,320,3233,388,3109,3122,774,488,3362,24]
for id in ins_ids:
	try:
		logging.info('Start:id=%s',id)
		ins_crawler=InsuranceCrawler(id)
		ins_crawler.fix_baofei()
	except BaseException,e:
		logging.error('Failed:id=%s,error=%s',id,e)
		raise

logging.info('Rate crawl finish!!!')
