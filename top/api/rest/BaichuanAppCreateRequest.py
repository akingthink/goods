'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class BaichuanAppCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.callbackurl = None
		self.description = None
		self.logo = None
		self.name = None

	def getapiname(self):
		return 'taobao.baichuan.app.create'

	def getMultipartParas(self):
		return ['logo']
