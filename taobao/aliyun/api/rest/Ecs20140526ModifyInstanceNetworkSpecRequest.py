'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20140526ModifyInstanceNetworkSpecRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.InstanceId = None
		self.InternetMaxBandwidthIn = None
		self.InternetMaxBandwidthOut = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyInstanceNetworkSpec.2014-05-26'
