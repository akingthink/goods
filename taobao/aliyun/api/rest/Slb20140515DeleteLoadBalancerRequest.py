'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Slb20140515DeleteLoadBalancerRequest(RestApi):
	def __init__(self,domain='slb.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.LoadBalancerId = None

	def getapiname(self):
		return 'slb.aliyuncs.com.DeleteLoadBalancer.2014-05-15'
