'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class WlbWaybillShengxianGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_code = None
		self.delivery_type = None
		self.feature = None
		self.order_channels_type = None
		self.sender_address_id = None
		self.service_code = None
		self.trade_id = None

	def getapiname(self):
		return 'taobao.wlb.waybill.shengxian.get'
