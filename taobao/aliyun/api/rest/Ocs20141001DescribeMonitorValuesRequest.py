'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ocs20141001DescribeMonitorValuesRequest(RestApi):
	def __init__(self,domain='ocs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.InstanceIds = None
		self.MonitorKeys = None

	def getapiname(self):
		return 'ocs.aliyuncs.com.DescribeMonitorValues.2014-10-01'
