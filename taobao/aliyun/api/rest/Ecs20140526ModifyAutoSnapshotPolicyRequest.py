'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20140526ModifyAutoSnapshotPolicyRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DataDiskPolicyEnabled = None
		self.DataDiskPolicyRetentionDays = None
		self.DataDiskPolicyRetentionLastWeek = None
		self.DataDiskPolicyTimePeriod = None
		self.SystemDiskPolicyEnabled = None
		self.SystemDiskPolicyRetentionDays = None
		self.SystemDiskPolicyRetentionLastWeek = None
		self.SystemDiskPolicyTimePeriod = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyAutoSnapshotPolicy.2014-05-26'
