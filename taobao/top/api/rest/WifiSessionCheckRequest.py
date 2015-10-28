'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class WifiSessionCheckRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.equip_id = None
		self.session_id = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.wifi.session.check'
