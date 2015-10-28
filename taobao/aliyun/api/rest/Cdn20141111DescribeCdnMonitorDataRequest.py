'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Cdn20141111DescribeCdnMonitorDataRequest(RestApi):
	def __init__(self,domain='cdn.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DomainName = None
		self.EndTime = None
		self.StartTime = None

	def getapiname(self):
		return 'cdn.aliyuncs.com.DescribeCdnMonitorData.2014-11-11'
