# -*- coding:utf-8 -*-

import qiniu
from qiniu import Auth
from qiniu import BucketManager
from qiniu import put_file


class Tool:

    """docstring for qi"""

    def __init__(self):
        self.access_key = 'O56byGVDbfXq1NoMFLQv5yG9Jn8ooTHKpIXaSxwz'
        self.secret_key = 'buC8FERvDoKmxpsN3wzUhyGR1QuN1AfGudJHOt3v'
        q = Auth(self.access_key, self.secret_key)
        self.bucket_name = 'yang-mblog'
        self.domain = 'http://7o51sj.com1.z0.glb.clouddn.com/'
        self.bucket = BucketManager(q)

    def get_pic(self, url):
        file_name = hash(url)
        ret, info = self.bucket.fetch(url, self.bucket_name, file_name)
        file_url = self.domain + str(file_name)
        return file_url
