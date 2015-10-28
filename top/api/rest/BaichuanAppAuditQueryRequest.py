'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class BaichuanAppAuditQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.user_appkey = None

	def getapiname(self):
		return 'taobao.baichuan.app.audit.query'
