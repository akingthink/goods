'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class SpContentDeletetagRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.site_key = None
		self.tagname = None

	def getapiname(self):
		return 'taobao.sp.content.deletetag'
