'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DmpDpeffectfeedbackGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.columns = None
		self.page = None
		self.page_size = None
		self.tb_user_id = None
		self.thedate = None

	def getapiname(self):
		return 'taobao.dmp.dpeffectfeedback.get'
