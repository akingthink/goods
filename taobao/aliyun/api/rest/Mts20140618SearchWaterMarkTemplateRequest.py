'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Mts20140618SearchWaterMarkTemplateRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.PageNumber = None
		self.PageSize = None
		self.State = None

	def getapiname(self):
		return 'mts.aliyuncs.com.SearchWaterMarkTemplate.2014-06-18'
