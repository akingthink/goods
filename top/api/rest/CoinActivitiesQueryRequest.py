'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CoinActivitiesQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.create_time_from = None
		self.create_time_to = None
		self.end_time_from = None
		self.end_time_to = None
		self.out_activity_ids = None
		self.page = None
		self.page_size = None
		self.start_time_from = None
		self.start_time_to = None
		self.status = None
		self.tb_activity_ids = None

	def getapiname(self):
		return 'taobao.coin.activities.query'
