'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class AlibabaInteractActivityRegisterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_id = None
		self.description = None
		self.end_time = None
		self.has_valid_time = None
		self.name = None
		self.picture = None
		self.start_time = None

	def getapiname(self):
		return 'alibaba.interact.activity.register'
