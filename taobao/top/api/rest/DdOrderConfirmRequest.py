'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdOrderConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cashier_orderid = None
		self.code = None
		self.items = None
		self.message = None
		self.orderid = None
		self.seller_usernick = None
		self.status = None

	def getapiname(self):
		return 'taobao.dd.order.confirm'
