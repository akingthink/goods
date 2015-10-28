'''
Created by auto_sdk on 2015-01-20 12:44:31
'''
from top.api.base import RestApi
class AlitripFlightinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.airline_code = None
		self.arr_airport = None
		self.cabin = None
		self.channel_name = None
		self.dep_airport = None
		self.dep_date = None
		self.flight_no = None
		self.password = None
		self.price = None

	def getapiname(self):
		return 'taobao.alitrip.flightinfo.get'
