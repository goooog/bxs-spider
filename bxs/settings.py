# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'SERVERID':'c5a543d925683d6d8b4ca9db97b8544d|1490620515|1490620415',
	'token':'e7f872db1a3045d1ad0e72bd1006a652',
	'user_id':'5D3687484C18F58D8B37F6555D4D092C',
	'JSESSIONID':'F0B81CBB4DB0ADF98701872F6A9B9D71'
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



