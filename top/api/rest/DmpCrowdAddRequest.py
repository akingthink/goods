'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DmpCrowdAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.crowd_name = None
		self.lookalike_multiple = None
		self.selects = None
		self.valid_date = None

	def getapiname(self):
		return 'taobao.dmp.crowd.add'
