# -*- coding:utf-8 -*-
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

reload(sys)
sys.setdefaultencoding('utf-8')

COOKIES={
	'er_id':'7074d7c9-7f5f-4103-9064-300e5e0d49e8',
	'Hm_lvt_59c99e4444d9fb864780844a90b61aea':'1488289573,1489677550',
	'Hm_lpvt_59c99e4444d9fb864780844a90b61aea':'1489680723',
	'JSESSIONID':'47587742B313779E1FBC841EE096B2A6',
	'token':'73f6911eb3684c2c8624ce3011629ebe',
	'user_id':'423BB8291945C985EC922FAFE5458D7B',
	'gr_session_id_b9b061e151df5788':'538d5f91-6cf6-4633-a3ca-e5cd765ff9b7',
	'gr_cs1_538d5f91-6cf6-4633-a3ca-e5cd765ff9b7':'user_id%3A423BB8291945C985EC922FAFE5458D7B', 
	'SERVERID':'ba8e961e5dc104c2f9dd3acf74fe712f|1489814767|1489814390'
}

DEFAULT_HEADERS=dict()

HOST='https://app.winbaoxian.com'

GET_PB_URL=HOST+'/planBook/combinePB/getAvailablePB'
CREAT_PB_URL=HOST+'/planBook/CombinePlanBookOutput/ajaxGet'
PB_RESULT_URL=HOST+'/planBook/planBookResult?nw=1&isCombine=1&id=%s'


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




