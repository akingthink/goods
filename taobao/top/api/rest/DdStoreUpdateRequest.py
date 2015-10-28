'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdStoreUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.brand = None
		self.businesstime = None
		self.contact = None
		self.out_storeid = None
		self.pic = None
		self.seller_usernick = None
		self.status = None

	def getapiname(self):
		return 'taobao.dd.store.update'
