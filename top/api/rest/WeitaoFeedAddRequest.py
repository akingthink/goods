'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class WeitaoFeedAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cover_pic = None
		self.json_tiles = None
		self.link = None
		self.link_desc = None
		self.show_detail = None
		self.title = None
		self.url_param = None

	def getapiname(self):
		return 'taobao.weitao.feed.add'
