'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class WangwangEserviceNewloginlogsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.btime = None
		self.etime = None
		self.query_ids = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.newloginlogs.get'
