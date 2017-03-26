# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'JSESSIONID':'162A9048B841B17A4DCDCF0B2FD19444',
	'SERVERID':'0566107f0b6ad539dab2d166a3543cea|1490525018|1490524847',
	'token':'ddb4465217e6419c8e4e143dcc26f22f',
	'user_id':'0BE3207603E77E5FF9C11D0585165407'
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



