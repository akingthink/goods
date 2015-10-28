'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from aliyun.api.base import RestApi
class Yundun20140924SetSLBDdosSettingRequest(RestApi):
	def __init__(self,domain='yundun.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.bps = None
		self.instanceId = None
		self.isLayer7 = None
		self.pps = None
		self.qps = None
		self.sipConn = None
		self.sipNew = None

	def getapiname(self):
		return 'yundun.aliyuncs.com.setSLBDdosSetting.2014-09-24'
