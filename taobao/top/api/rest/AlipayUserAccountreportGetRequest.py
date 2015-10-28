'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class AlipayUserAccountreportGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'alipay.user.accountreport.get'
