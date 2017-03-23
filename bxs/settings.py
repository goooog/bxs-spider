# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'JSESSIONID':'423BB8291945C985EC922FAFE5458D7B',
	'SERVERID':'40c64587d2f26f6bb62cb954d12bbc22|1490292824|1490292798',
	'token':'b3e375b2ec5b41268fedc4054fb915d3',
	'user_id':'423BB8291945C985EC922FAFE5458D7B'
}

DEFAULT_HEADERS=dict()

HOST='https://app.winbaoxian.com'

GET_PB_URL=HOST+'/planBook/combinePB/getAvailablePB'
GET_VERIFY_URL=HOST+'/planBook/combinePB/getVerifyValue'
CALCULATE_PB_URL=HOST+'/planBook/combinePB/calculate'
CREAT_PB_URL=HOST+'/planBook/CombinePlanBookOutput/ajaxGet'
PB_PAGE_URL=HOST+'/planBook/planBookResult?nw=1&isCombine=1&id='


COMMON_DATA={
	"sex":1,
	"age":0,
	"isApply":False,
	"applySex":1,
	"applyAge":18,
	"isReceive":True,
	"csex":1,
	"isShuangHm":False,
	"sHmSex":2,
	"sHmAge":18
}




