'''
Created by auto_sdk on 2015-01-20 12:44:32
'''
from top.api.base import RestApi
class DdImgUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image = None
		self.item_id = None
		self.out_storeid = None
		self.remote_url = None
		self.seller_usernick = None
		self.type = None

	def getapiname(self):
		return 'taobao.dd.img.upload'

	def getMultipartParas(self):
		return ['image']
