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
        self.shop_dict = {"京东商城": "JD",
                          "易迅网": "yixun",
                          "天猫": "Tmall",
                          "amazon": "Amazon",
                          "Lookfantastic": "haitao",
                          "1号店": "yhd",
                          "苏宁易购": "suning",
                          "6pm": "6pm",
                          "当当网": "dangdang",
                          "新蛋中国": "newegg",
                          "亚马逊": "Amazon",
                          "亚马逊中国": "Amazon",
                          "ESTEELAUDER美国官网": "haitao",
                          "当当": "dangdang",
                          "Ashford": "haitao",
                          "TORYBURCH美国官网": "haitao",
                          "惠惠网": "huihui",
                          "日本亚马逊": "JAmazon",
                          "国美在线": "gmone",
                          "健一网": "jianyi",
                          "华强北商城": "huaqiang",
                          "优购时尚商城": "other",
                          "新蛋商城": "newegg",
                          "易迅商城": "yixun",
                          "天猫国际": "Tmall_H",
                          "RalphLauren美国官网": "haitao",
                          "沱沱工社": "other",
                          "考拉海购": "haitao",
                          "kipling美国官网": "haitao",
                          "huihui": "huihui",
                          "Woot": "haitao",
                          "ebay": "haitao",
                          "京东全球购": "JD_H",
                          "GNC": "haitao",
                          "HQhair": "haitao",
                          "蜜芽宝贝": "miya",
                          "steam": "haitao",
                          "kidsroom.de": "haitao",
                          "1元夺宝": "other",
                          "NeimanMarcus": "haitao",
                          "壹药网": "yiyao",
                          "iHerb": "haitao",
                          "RebeccaMinkoff美国官网": "haitao",
                          "MANKIND": "haitao",
                          "淘宝网": "taobao",
                          "阿里旅行": "other",
                          "jomashop": "haitao",
                          "MYBAG": "haitao"}

    def update_goods_last_spider_logs(self, source, goods_count, newest_url):
        goods_last_spider_logs = self.db.goods_last_spider_logs
        goods_last_spider_logs.update(
            {'source': source}, {'source': source, 'goods_count': goods_count, 'newest_url': newest_url, 'spider_time': datetime.datetime.now()}, True)

    def update_goods_count(self, source, goods_count):
        goods_spider_logs = self.db.goods_spider_logs
        goods_newest_spider_logs = self.db.goods_newest_spider_logs
        prev_goods_spider_logs = goods_spider_logs.find().sort(
            "created_time", DESCENDING).limit(1)
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

    def get_goods_shop(self, shop_name):
        goods_shops = self.db.goods_shops
        goods_shop = goods_shops.find_one({'shop_name': shop_name})
        try:
            shop_code = self.shop_dict[shop_name]
        except Exception:
            shop_code = "other"
        goods_count = 1 if goods_shop is None else int(
            goods_shop['goods_count']) + 1
        goods_shops.update({"shop_name": shop_name},
                           {'shop_code': shop_code, 'shop_name': shop_name, "goods_count": goods_count, "created_time": datetime.datetime.now()}, True)
