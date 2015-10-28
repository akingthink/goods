'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class LogisticsInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ab_cn_code = None
		self.ab_cp_code = None
		self.cp_code = None
		self.is_waybill = None
		self.mail_no = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.info.get'
