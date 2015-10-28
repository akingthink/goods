'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class AlitripOrderinfoAirbookRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.book_arranger_info = None
		self.book_flight_segment_list = None
		self.book_traveler_list = None
		self.channel_name = None
		self.extra = None
		self.fee = None
		self.password = None
		self.payment = None
		self.reservation_code = None
		self.tax = None
		self.total_money = None

	def getapiname(self):
		return 'taobao.alitrip.orderinfo.airbook'
