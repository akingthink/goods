'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class VmarketEticketManageNotifyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.codemerchant_id = None
		self.notify_method = None
		self.order_id = None

	def getapiname(self):
		return 'taobao.vmarket.eticket.manage.notify'
