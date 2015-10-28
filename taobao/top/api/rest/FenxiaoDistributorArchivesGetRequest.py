'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class FenxiaoDistributorArchivesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.distributor_user_nick = None

	def getapiname(self):
		return 'taobao.fenxiao.distributor.archives.get'
