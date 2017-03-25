#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bxs.ins_crawler import InsuranceCrawler

#ins_crawler=InsuranceCrawler(634)
ins_ids=range(461,812)+range(3067,4000)
for id in ins_ids:
	try:
		print 'Start:',id
		ins_crawler=InsuranceCrawler(id)
		ins_crawler.run_fee()
	except BaseException,e:
		print 'Failed:', id
print 'finish!!!!!'
