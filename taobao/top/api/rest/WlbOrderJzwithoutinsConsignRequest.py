'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class WlbOrderJzwithoutinsConsignRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.jz_consign_args = None
		self.tid = None
		self.tms_partner = None

	def getapiname(self):
		return 'taobao.wlb.order.jzwithoutins.consign'
