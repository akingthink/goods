'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class ItemQualificationCheckRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.name = None
		self.value = None

	def getapiname(self):
		return 'taobao.item.qualification.check'
