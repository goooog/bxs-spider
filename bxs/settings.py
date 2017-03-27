# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'JSESSIONID':'F0B81CBB4DB0ADF98701872F6A9B9D71',
	'SERVERID':'c5a543d925683d6d8b4ca9db97b8544d|1490613540|1490613532',
	'token':'faf06287cf0642c4af6de9fadaf605f6',
	'user_id':'64456AFCF839A520F117931CDD8E7AC8'
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

DB_CONFIG=dict(
	host='localhost',
	port=3306,
	user='root',
	passwd='',
	database='bxs'
)



