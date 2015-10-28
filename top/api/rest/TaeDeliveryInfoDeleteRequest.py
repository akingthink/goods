'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class TaeDeliveryInfoDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.out_id = None

	def getapiname(self):
		return 'taobao.tae.delivery.info.delete'
