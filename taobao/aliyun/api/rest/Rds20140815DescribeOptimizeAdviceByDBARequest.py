'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeOptimizeAdviceByDBARequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DBInstanceId = None
		self.PageNumber = None
		self.PageSize = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeOptimizeAdviceByDBA.2014-08-15'
