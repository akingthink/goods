'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20140526ModifyVRouterAttributeRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.Description = None
		self.VRouterId = None
		self.VRouterName = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyVRouterAttribute.2014-05-26'
