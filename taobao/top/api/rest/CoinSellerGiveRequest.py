'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CoinSellerGiveRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.amount = None
		self.attributes = None
		self.comments = None
		self.out_id = None
		self.seller_id = None
		self.tb_activity_id = None
		self.token = None

	def getapiname(self):
		return 'taobao.coin.seller.give'
