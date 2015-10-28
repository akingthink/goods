'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class AlitripOrderinfoOfficereauthorizeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.new_office_id = None
		self.office_id = None
		self.pnr = None
		self.tc_order_id = None

	def getapiname(self):
		return 'taobao.alitrip.orderinfo.officereauthorize'
