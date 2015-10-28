'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class WeitaoCloudtagsGroupCustomAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.group_desc = None
		self.group_name = None
		self.user_list_file_content = None

	def getapiname(self):
		return 'taobao.weitao.cloudtags.group.custom.add'

	def getMultipartParas(self):
		return ['user_list_file_content']
