'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20130110LeaveSecurityGroupRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.InstanceId = None
		self.SecurityGroupId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.LeaveSecurityGroup.2013-01-10'