'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class VmarketEticketAuthConsumeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.consume_num = None
		self.operatorid = None
		self.serial_num = None
		self.storeid = None
		self.verify_code = None

	def getapiname(self):
		return 'taobao.vmarket.eticket.auth.consume'
