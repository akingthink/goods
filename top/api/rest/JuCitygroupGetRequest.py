'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class JuCitygroupGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.city = None
		self.fields = None

	def getapiname(self):
		return 'taobao.ju.citygroup.get'
