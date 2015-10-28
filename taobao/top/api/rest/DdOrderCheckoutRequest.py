'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdOrderCheckoutRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cashier_orderid = None
		self.contact = None
		self.items = None
		self.out_storeid = None
		self.people = None
		self.promotioninfo = None
		self.realprice = None
		self.seller_usernick = None
		self.tablenumber = None
		self.tb_orderid = None
		self.totalprice = None

	def getapiname(self):
		return 'taobao.dd.order.checkout'
