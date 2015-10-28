'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ocs20141001ModifySecurityIpsRequest(RestApi):
	def __init__(self,domain='ocs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.InstanceId = None
		self.SecurityIps = None

	def getapiname(self):
		return 'ocs.aliyuncs.com.ModifySecurityIps.2014-10-01'
