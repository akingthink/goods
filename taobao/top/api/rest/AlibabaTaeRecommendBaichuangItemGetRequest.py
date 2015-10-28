'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class AlibabaTaeRecommendBaichuangItemGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.open_uid = None

	def getapiname(self):
		return 'alibaba.tae.recommend.baichuang.item.get'
