'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20140526DescribeDiskMonitorDataRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DiskId = None
		self.EndTime = None
		self.Period = None
		self.StartTime = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DescribeDiskMonitorData.2014-05-26'
