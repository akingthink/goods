'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class BaichuanAppOnlineApplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.apk_package = None
		self.apply_params = None
		self.mrd_file = None
		self.operator_ip = None
		self.user_appkey = None

	def getapiname(self):
		return 'taobao.baichuan.app.online.apply'

	def getMultipartParas(self):
		return ['apk_package','mrd_file']
