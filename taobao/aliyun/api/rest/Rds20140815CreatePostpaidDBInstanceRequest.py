'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Rds20140815CreatePostpaidDBInstanceRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.ClientToken = None
		self.DBInstanceClass = None
		self.DBInstanceDescription = None
		self.DBInstanceNetType = None
		self.DBInstanceStorage = None
		self.Engine = None
		self.EngineVersion = None
		self.RegionId = None
		self.SecurityIPList = None

	def getapiname(self):
		return 'rds.aliyuncs.com.CreatePostpaidDBInstance.2014-08-15'