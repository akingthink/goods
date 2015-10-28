'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class AthenaItemSolutionAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.question = None
		self.solution = None
		self.solution_level = None
		self.solution_stf = None
		self.type_key = None

	def getapiname(self):
		return 'taobao.athena.item.solution.add'
