'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class WeitaoCommentsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.direction = None
		self.feed_id = None
		self.page_size = None
		self.time_stamp = None

	def getapiname(self):
		return 'taobao.weitao.comments.get'
