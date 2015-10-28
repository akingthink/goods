'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class BaichuanIsvCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.email = None
		self.name = None
		self.phone = None

	def getapiname(self):
		return 'taobao.baichuan.isv.create'
