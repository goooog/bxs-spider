#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import logging
import re
import time

from loggings import *
from settings import *

def is_http_ok(response):
	return response and response.status_code==requests.codes.ok

def http_post(url,payload):
	max_retry=6
	for i in range(0,max_retry):
		try:
			time.sleep(1)
			r=requests.post(url,data=payload,cookies=COOKIES,verify=False,timeout=10)
			return r
		except requests.exceptions.RequestException,e:
			logging.error('Http error:%s',e)

def http_get(url):
	max_retry=6
	for i in range(0,max_retry):
		try:
			time.sleep(1)
			r=requests.get(url,cookies=COOKIES,verify=False,timeout=10)
			return r
		except requests.exceptions.RequestException,e:
			logging.error('Http error:%s',e)

def str2int(value):
	if not isinstance(value,basestring):
		return
	if value=='趸交':
		return 1
	elif value=='终身':
		return 100
	match=re.match(r'.*?(\d+).*',value)
	if match:
		return match.group(1)
	else:
		logging.warning('not matched:%s',value)
		return ''
