'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class CaipiaoPresentWinItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.date = None
		self.num = None
		self.page_no = None
		self.search_type = None

	def getapiname(self):
		return 'taobao.caipiao.present.win.items.get'
