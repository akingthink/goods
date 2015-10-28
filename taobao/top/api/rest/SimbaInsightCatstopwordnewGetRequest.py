'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class SimbaInsightCatstopwordnewGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat_id = None
		self.dimension = None
		self.end_date = None
		self.page_size = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.simba.insight.catstopwordnew.get'
