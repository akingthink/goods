'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ocs20141001ModifyInstanceCapacityRequest(RestApi):
	def __init__(self,domain='ocs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.Capacity = None
		self.InstanceId = None

	def getapiname(self):
		return 'ocs.aliyuncs.com.ModifyInstanceCapacity.2014-10-01'
