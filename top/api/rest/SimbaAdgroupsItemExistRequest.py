'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class SimbaAdgroupsItemExistRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.item_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroups.item.exist'
