'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CoinBuyerDetailsQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.create_time_from = None
		self.create_time_to = None
		self.out_ids = None
		self.page = None
		self.page_size = None
		self.type = None

	def getapiname(self):
		return 'taobao.coin.buyer.details.query'
