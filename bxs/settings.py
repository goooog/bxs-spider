# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'JSESSIONID':'F0B81CBB4DB0ADF98701872F6A9B9D71',
	'SERVERID':'ba8e961e5dc104c2f9dd3acf74fe712f|1490545931|1490545907',
	'token':'e82affb36385434da0a6e62d9f12a959',
	'user_id':'7B9210C1EBEC50CBDF28EEE673319C2F'
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



