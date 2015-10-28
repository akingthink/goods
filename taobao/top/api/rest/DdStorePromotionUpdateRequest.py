'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdStorePromotionUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.descinfo = None
		self.discount = None
		self.end_time = None
		self.out_storeid = None
		self.seller_usernick = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'taobao.dd.store.promotion.update'
