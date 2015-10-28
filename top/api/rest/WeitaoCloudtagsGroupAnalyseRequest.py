'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class WeitaoCloudtagsGroupAnalyseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.analyze_expression = None
		self.group_expression = None

	def getapiname(self):
		return 'taobao.weitao.cloudtags.group.analyse'
