'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class CrmGradeSetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.amount = None
		self.count = None
		self.discount = None
		self.grade = None
		self.hierarchy = None

	def getapiname(self):
		return 'taobao.crm.grade.set'
