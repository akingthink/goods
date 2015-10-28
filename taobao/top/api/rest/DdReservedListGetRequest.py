'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdReservedListGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.buyer_phone = None
		self.create_end = None
		self.create_start = None
		self.ends = None
		self.option = None
		self.out_storeid = None
		self.pn = None
		self.ps = None
		self.seller_usernick = None
		self.starts = None
		self.status = None

	def getapiname(self):
		return 'taobao.dd.reserved.list.get'
