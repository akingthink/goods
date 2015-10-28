'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdItemAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_tag = None
		self.currentprice = None
		self.desc = None
		self.hot = None
		self.id = None
		self.image = None
		self.isdiscount = None
		self.isnew = None
		self.isrecommend = None
		self.issetfood = None
		self.istakeout = None
		self.item_category_id = None
		self.item_category_name = None
		self.item_category_parentid = None
		self.item_category_sort = None
		self.name = None
		self.pic = None
		self.price = None
		self.properties = None
		self.propertiesvalue = None
		self.seller_usernick = None
		self.setfood = None
		self.setfoodlist = None
		self.sort = None
		self.stock = None
		self.storeid = None
		self.sync_version = None
		self.taste = None
		self.unit = None

	def getapiname(self):
		return 'taobao.dd.item.add'

	def getMultipartParas(self):
		return ['image']

	def getTranslateParas(self):
		return {'item_category_sort':'item_category.sort','item_category_name':'item_category.name','item_category_id':'item_category.id','item_category_parentid':'item_category.parentid'}
