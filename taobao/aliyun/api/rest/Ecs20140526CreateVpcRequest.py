'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ecs20140526CreateVpcRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.CidrBlock = None
		self.ClientToken = None
		self.Description = None
		self.RegionId = None
		self.VpcName = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.CreateVpc.2014-05-26'