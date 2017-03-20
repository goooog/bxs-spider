# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'gr_user_id':'35fceb4a-adb3-4565-88b3-b6c25ef7272b',
	'Hm_lvt_59c99e4444d9fb864780844a90b61aea':'1488289573,1489677550,1489938796',
	'Hm_lpvt_59c99e4444d9fb864780844a90b61aea':'1489938948',
	'JSESSIONID':'31B8723721108CB4A5B72C602970EFA5',
	'SERVERID':'ba8e961e5dc104c2f9dd3acf74fe712f|1490017982|1489938796',
	'token':'9dfd18b6c46842e6af35a35febf9e77f',
	'user_id':'423BB8291945C985EC922FAFE5458D7B'
}

DEFAULT_HEADERS=dict()

HOST='https://app.winbaoxian.com'

GET_PB_URL=HOST+'/planBook/combinePB/getAvailablePB'
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




