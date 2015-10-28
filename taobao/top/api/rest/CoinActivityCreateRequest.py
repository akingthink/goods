'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CoinActivityCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_title = None
		self.activity_url = None
		self.budget_amount = None
		self.end_time = None
		self.feature = None
		self.out_activity_id = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.coin.activity.create'
