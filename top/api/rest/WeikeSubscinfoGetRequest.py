'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class WeikeSubscinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_num = None
		self.seller_name = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.weike.subscinfo.get'
