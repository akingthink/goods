# -*- coding:utf-8 -*-
import pymongo
import datetime
from pymongo import DESCENDING


class Baseinfo:

    def __init__(self, host='localhost', port=27017, db_name='sales'):
        self.host = host
        self.port = port
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[db_name]

    def update_goods_last_spider_logs(self, source, goods_count, newest_url):
        goods_last_spider_logs = self.db.goods_last_spider_logs
        goods_last_spider_logs.update(
            {'source': source}, {'source': source, 'goods_count': goods_count, 'newest_url': newest_url, 'spider_time': datetime.datetime.now()}, True)

    def update_goods_count(self, source, goods_count):
        goods_spider_logs = self.db.goods_spider_logs
        goods_newest_spider_logs = self.db.goods_newest_spider_logs
        prev_goods_spider_logs = goods_spider_logs.find().sort("created_time", DESCENDING).limit(1)
        for item in prev_goods_spider_logs:
            prev_goods_spider_logs = item
        prev_total_count = prev_goods_spider_logs[
            'total_count'] if prev_goods_spider_logs is not None else 0
        total_count = int(prev_total_count) + int(goods_count)
        goods_spider_log = {'source': source, 'goods_count': goods_count,
                            'total_count': total_count, 'created_time': datetime.datetime.now()}
        goods_newest_spider_logs.update({'source': source}, {'source': source, 'goods_count': goods_count,
                                                             'total_count': total_count, 'created_time': datetime.datetime.now()}, True)
        goods_spider_logs.insert_one(goods_spider_log)

    def get_prev_url(self, source):
        goods_last_spider_logs = self.db.goods_last_spider_logs
        prev_url = goods_last_spider_logs.find_one(
            {'source': source})['newest_url'] if goods_last_spider_logs.find_one({'source': source}) is not None else ''
        return prev_url
