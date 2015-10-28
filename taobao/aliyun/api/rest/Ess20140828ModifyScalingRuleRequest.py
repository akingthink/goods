'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Ess20140828ModifyScalingRuleRequest(RestApi):
	def __init__(self,domain='ess.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.AdjustmentType = None
		self.AdjustmentValue = None
		self.Cooldown = None
		self.ScalingRuleId = None
		self.ScalingRuleName = None

	def getapiname(self):
		return 'ess.aliyuncs.com.ModifyScalingRule.2014-08-28'
