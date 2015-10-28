'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class SimbaInsightWordsareadataGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bidword = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.simba.insight.wordsareadata.get'
