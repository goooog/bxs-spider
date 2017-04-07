#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from bxs.profit import ProfitCrawler
from bxs.loggings import *

ins_ids=[3504,3505,3506,3508,457,481,482,483,484,524,557,3091,3121,3125,3153,3164,468,470,533,542,567,3069,3070,3072,3073,3087,3092,3094,3108,3124,3156,605,630,631,634,645,651,659,666,667,668,669,673,690,692,701,773,782,800,805,810,3158,3165,3169,3192,3193,3196,3214,3215,3217,3230,3244,3245,3260,3263,3264,3269,3289,3290,3291,3312,3314,3316,3317,3323,3326,3327,3352,3356,3357,3366,3375,3377,3378,3379,3380,3383,3384,3427,3495,3496,644,789,610,413]
for id in ins_ids:
	try:
		logging.info('Profit start:id=%s',id)
		profit_crawler=ProfitCrawler(id)
		profit_crawler.run()
	except BaseException,e:
		logging.error('Profit failed:id=%s,error=%s',id,e)
	
logging.info("Profit crawler finish")
