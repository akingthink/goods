'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Odps20141215OpenOdpsServiceRequest(RestApi):
	def __init__(self,domain='odps.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None

	def getapiname(self):
		return 'odps.aliyuncs.com.OpenOdpsService.2014-12-15'
