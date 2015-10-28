'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class RdsDbCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.db_name = None
		self.instance_name = None

	def getapiname(self):
		return 'taobao.rds.db.create'
