'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class VmarketEticketCardBeforeconsumeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.codemerchant_id = None
		self.id_card = None
		self.order_id = None
		self.posid = None
		self.token = None

	def getapiname(self):
		return 'taobao.vmarket.eticket.card.beforeconsume'
