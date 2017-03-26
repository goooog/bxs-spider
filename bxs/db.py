#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from loggings import *
from settings import DB_CONFIG
from tools import str2int

import MySQLdb

	

class DBUtil:
	def __init__(self):
		self.host=DB_CONFIG['host']
		self.port=DB_CONFIG['port']
		self.user=DB_CONFIG['user']
		self.passwd=DB_CONFIG['passwd']
		self.db=DB_CONFIG['database']
		
	def __get_connection(self):
		return MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset='utf8')

	def execute(self,sql,args,is_insert=False):
		conn=None
		cur=None
		ret=None
		try:
			conn=self.__get_connection()
			cur=conn.cursor()
			cur.execute(sql,args)
			
			if is_insert:
				ret=conn.insert_id()
			conn.commit()
		except BaseException,e:
			print 'exception:',e
			if conn:
				conn.rollback()
			raise
		finally:
			if cur:
				cur.close()
			if conn:
				conn.close()
		return ret
				
	def delete_by_id(self,sql,_id):
		return self.execute(sql,[_id])

	
	def insert(self,sql,args):
		return self.execute(sql,args,True)	
	
class ProfitDao:
	def __init__(self):
		self.db=DBUtil()
	
	def save_profits(self,profits,profit_id,insurance_id):
		if not isinstance(profits,dict):
			logging.warning('Invalid profits:%s',profits)
			return
		self.__save_profit_list(profits.get('profitHigh'),profit_id,'H',insurance_id)
		self.__save_profit_list(profits.get('profitMiddle'),profit_id,'M',insurance_id)
		self.__save_profit_list(profits.get('profitLow'),profit_id,'L',insurance_id)
	
	
	def __save_profit_list(self,profit,pid,profit_grade,insurance_id):
		if not isinstance(profit,list) or len(profit)==0:
			return
		for data in profit:
			name=data.get('name')
			self.__save_profit_value(pid,data.get('high'),profit_grade,'H',name,insurance_id)
			self.__save_profit_value(pid,data.get('middle'),profit_grade,'M',name,insurance_id)
			self.__save_profit_value(pid,data.get('low'),profit_grade,'L',name,insurance_id)

	def __save_profit_value(self,pid,profit_value,profit_grade,wanneng_grade,name,insurance_id):
		if not isinstance(profit_value,list) or len(profit_value)==0:
			return
		sql='INSERT INTO insurance_profit_value ( `profit_id`, `insurance_id`, `name`, `money`, `wanneng_grade`, `profit_grade`, `policy_year`) VALUES(%s,%s,%s,%s,%s,%s,%s)'
		i=1
		for v in profit_value:
			value=[pid,insurance_id,name,v,wanneng_grade,profit_grade,i]	
			self.db.insert(sql,value)
			i=i+1
			
	
	def delete_profits(self,insurance_id):
		self.db.delete_by_id('delete from insurance_profit_variable where insurance_id=%s',insurance_id)
		self.db.delete_by_id('delete from insurance_profit_value where insurance_id=%s',insurance_id)


class InsuranceDao:
	def __init__(self):
		self.db=DBUtil()
	
	def delete(self,insurance_id):
		self.db.delete_by_id('delete from insurance_rate where insurance_id=%s',insurance_id)
	
	
	def save_insurance(self,table,insurance):
		if not isinstance(insurance,dict):
			logging.warning('invalid insurance:%s',insurance)
			return

		common_data=insurance['commonData']
		ins_id=insurance['insuranceTypeId']
		ins_pingyin=insurance['allMainInsData'].keys()[0]
		ins=insurance['allMainInsData'][ins_pingyin]
		bao_type=ins['baoType']
		main_ins=ins[bao_type]	

		sql='insert into '+table+'(insurance_id, insurance_name, sex, age, years, baoe, baof, lingqu, duration, lingqu_type, smoke, social, plan)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		args=[]
		args.append(ins_id)
		args.append(main_ins.get('name'))
		args.append(common_data.get('sex'))
		args.append(common_data.get('age'))
		args.append(main_ins.get('years'))
		args.append(main_ins.get('baoe'))
		args.append(main_ins.get('baof'))
		args.append(main_ins.get('lingqu'))
		args.append(str2int(main_ins.get('duration')))
		args.append(main_ins.get('lingquTyp'))
		args.append(main_ins.get('smoke'))
		args.append(main_ins.get('social'))
		args.append(main_ins.get('plan'))
		
		return self.db.insert(sql,args)
		
