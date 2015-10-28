'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DmpAnalysisChartGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.selects = None
		self.tag_id = None

	def getapiname(self):
		return 'taobao.dmp.analysis.chart.get'
