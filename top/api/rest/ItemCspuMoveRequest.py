'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class ItemCspuMoveRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.sku_cspu_mapping = None
		self.sku_mealproperty_mapping = None
		self.spu_id = None

	def getapiname(self):
		return 'taobao.item.cspu.move'
