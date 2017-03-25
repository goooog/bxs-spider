# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'JSESSIONID':'C5E671BBFF5A26EF712F8CC4D60E5DE3',
	'SERVERID':'40c64587d2f26f6bb62cb954d12bbc22|1490426096|1490422163',
	'token':'dda8999abb74425d89daeb39130faa81',
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




