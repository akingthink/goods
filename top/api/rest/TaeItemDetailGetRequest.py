'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class TaeItemDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_ip = None
		self.fields = None
		self.id = None

	def getapiname(self):
		return 'taobao.tae.item.detail.get'
