'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class TopatsJushitaJdpDatadeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.start_modified = None
		self.sync_type = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.topats.jushita.jdp.datadelete'
