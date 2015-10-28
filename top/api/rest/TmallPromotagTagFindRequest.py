'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class TmallPromotagTagFindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.tag_id = None
		self.tag_name = None

	def getapiname(self):
		return 'tmall.promotag.tag.find'
