'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class SpShopInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.seller_id = None
		self.site_key = None

	def getapiname(self):
		return 'taobao.sp.shop.info.get'
