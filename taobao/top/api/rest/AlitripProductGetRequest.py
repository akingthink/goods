'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class AlitripProductGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.airline = None
		self.channel_name = None
		self.end_time = None
		self.extra = None
		self.page_no = None
		self.page_size = None
		self.password = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.alitrip.product.get'
