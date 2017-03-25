#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bxs.ins_crawler import InsuranceCrawler

ins_crawler=InsuranceCrawler(634)
combinations=ins_crawler.run_fee()
print 'finish!!!!!'
