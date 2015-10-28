'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class FenxiaoDistributorProcuctStaticGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.distributor_user_nick = None
		self.product_id_array = None

	def getapiname(self):
		return 'taobao.fenxiao.distributor.procuct.static.get'
