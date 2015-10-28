'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdStorePromotionGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.out_storeid = None
		self.page_no = None
		self.page_size = None
		self.seller_usernick = None
		self.type = None

	def getapiname(self):
		return 'taobao.dd.store.promotion.get'
