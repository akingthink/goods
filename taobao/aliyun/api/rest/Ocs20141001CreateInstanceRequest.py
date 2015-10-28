'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ocs20141001CreateInstanceRequest(RestApi):
	def __init__(self,domain='ocs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.Capacity = None
		self.InstanceName = None
		self.Password = None
		self.RegionId = None
		self.Token = None
		self.ZoneId = None

	def getapiname(self):
		return 'ocs.aliyuncs.com.CreateInstance.2014-10-01'
