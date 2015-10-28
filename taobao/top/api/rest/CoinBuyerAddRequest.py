'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CoinBuyerAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.amount = None
		self.comments = None
		self.feature = None
		self.out_id = None
		self.out_parent_id = None
		self.token = None

	def getapiname(self):
		return 'taobao.coin.buyer.add'
