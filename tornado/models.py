# coding:utf-8
import concurrent.futures
import os.path
import re
import subprocess
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import mongoengine
import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

mongoengine.connect('sales', host='localhost', port=27017)


class Goods_summarys(mongoengine.Document):
    source_name = mongoengine.StringField()
    goods_title = mongoengine.StringField()
    goods_sub_title = mongoengine.StringField()
    goods_main_url = mongoengine.StringField()
    goods_ico = mongoengine.StringField()
    goods_type = mongoengine.StringField()
    passdue_tag = mongoengine.IntField()
    goods_id = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
    goods_content = mongoengine.StringField()
    shop_name = mongoengine.StringField()
    source = mongoengine.StringField()
    now = mongoengine.DateTimeField(default=datetime.datetime.now())
    meta = {
        'ordering': ['-created_at']
    }


class Goods_contents(mongoengine.Document):
    title = mongoengine.StringField()
    sub_title = mongoengine.StringField()
    goods_url = mongoengine.StringField()
    content_main = mongoengine.StringField()
    goods_id = mongoengine.StringField()
    now = mongoengine.DateTimeField(default=datetime.datetime.now())


class Goods_last_spider_logs(mongoengine.Document):
    source = mongoengine.StringField()
    spider_time = mongoengine.DateTimeField()
    newest_url = mongoengine.StringField()
    goods_count = mongoengine.IntField()
    now = mongoengine.DateTimeField(default=datetime.datetime.now())

    meta = {
        'ordering': ['-spider_time']
    }


class Goods_spider_logs(mongoengine.Document):
    source = mongoengine.StringField()
    goods_count = mongoengine.IntField()
    total_count = mongoengine.IntField()
    created_time = mongoengine.DateTimeField()
    now = mongoengine.DateTimeField(default=datetime.datetime.now())

    meta = {
        'ordering': ['-created_time']
    }


class Goods_newest_spider_logs(mongoengine.Document):
    source = mongoengine.StringField()
    goods_count = mongoengine.IntField()
    total_count = mongoengine.IntField()
    created_time = mongoengine.DateTimeField()
    now = mongoengine.DateTimeField(default=datetime.datetime.now())

    meta = {
        'ordering': ['-created_time']
    }
