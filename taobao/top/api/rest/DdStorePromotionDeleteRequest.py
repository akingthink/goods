'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdStorePromotionDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.out_storeid = None
		self.promotion_id = None
		self.seller_usernick = None

	def getapiname(self):
		return 'taobao.dd.store.promotion.delete'
