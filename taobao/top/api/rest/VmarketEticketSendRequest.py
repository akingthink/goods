'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class VmarketEticketSendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.codemerchant_id = None
		self.order_id = None
		self.qr_images = None
		self.token = None
		self.verify_codes = None

	def getapiname(self):
		return 'taobao.vmarket.eticket.send'
