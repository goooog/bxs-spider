#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bxs.fee_crawler import FeeCrawler
from bxs.ins_crawler import InsuranceCrawler

ins_crawler=InsuranceCrawler(634)
pb_datas=ins_crawler.run()

for pb in pb_datas:
	fee_crawler=FeeCrawler(pb)
	fee_crawler.run()
