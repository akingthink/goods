'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class SpContentCustomPublishRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.classname = None
		self.content = None
		self.detailurl = None
		self.site_key = None
		self.tags = None
		self.title = None

	def getapiname(self):
		return 'taobao.sp.content.custom.publish'
