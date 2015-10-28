# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
from lxml import html
import requests
from bs4 import BeautifulSoup
import pymongo
import datetime
import time
import qiniu_tool

conn = pymongo.MongoClient('localhost', 27017)
db = conn.sales
goods_summarys = db.goods_summarys
goods_contents = db.goods_contents
tool = qiniu_tool.Tool()
goods_spider_logs = db.goods_spider_logs
print goods_spider_logs.find_one()

for item in goods_spider_logs.find().sort({"created_time": 1}).limit(1):
    print item

# def has_data_log_but_no_class(tag):
#     return tag.has_attr('data-log') and not tag.has_attr('class')


# def convert_img_url(url):
#     return url + "==ywj"


# def update_url(content_main_div):
#     for item in content_main_div:
#         img_tag = item.find("img")
#         if img_tag:
#             img_tag['src'] = tool.get_pic(img_tag['src'])
#     return content_main_div


# def get_goods_detail(url, goods_id):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "lxml")
#     content_div = soup.find("div", "hui-list")
#     title = content_div.find("h1").find("a").string.encode('utf8').strip()
#     sub_title = content_div.find("h4").string.encode('utf8').strip()
#     pattern = '(^.*?)\?tag'
#     if re.findall(pattern, content_div.find("h1").find("a")['href']):
#         goods_url = re.findall(pattern, content_div.find("h1").find("a")['href'])[0]
#     else:
#         goods_url = content_div.find("h1").find("a")['href']
#     content_main_div = content_div.find_all("div", "editor-mod")
#     content_main = ""
#     for item in update_url(content_main_div):
#         content_main += str(item)
#     goods_content = {'title': title, 'sub_title': sub_title, 'goods_url': goods_url,
#                      'content_main': content_main, 'goods_id': goods_id}
#     goods_contents.insert_one(goods_content)


# def get_goods_info(url, prev_goods_main_url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "lxml")
#     content_div = soup.find_all("div", "module-hui-list-item1")
#     pattern = re.compile('\d+')
#     i = 1
#     for item in content_div:
#         goods_url_tag = item.find("a", href=re.compile('/deals/\d+'))
#         if goods_url_tag:
#             passdue_tag = 0 if item.find("div", "hui-list-ctn passdue  clearfix") == None else 1
#             shop_name = item.find("a", "shop").string.encode('utf8').strip() if item.find("a", "shop") != None else '其他'
#             goods_type = item.find("div", "list-shop").find(has_data_log_but_no_class).string.encode('utf8').strip()
#             goods_main_url = "http://www.huihui.cn" + goods_url_tag['href']
#             goods_id = str(hash(goods_main_url))
#             goods_ico = tool.get_pic(item.find("img")['data-src'])
#             goods_content = item.find("div", "hui-content-text").contents[1].contents[0].encode('utf8').strip()
#             if i == 1:
#                 begin_goods_main_url = goods_main_url
#                 i += 1
#             if goods_main_url != prev_goods_main_url:
#                 goods_summary = {'shop_name': shop_name, 'goods_type': goods_type,
#                                  'goods_main_url': goods_main_url, 'goods_ico': goods_ico,
#                                  'goods_content': goods_content, 'passdue_tag': passdue_tag,
#                                  'source': 'huihui.com', 'source_name': '惠惠',
#                                  'goods_id': goods_id,
#                                  'created_at': datetime.datetime.utcnow()}
#                 goods_summarys.insert_one(goods_summary)
#                 print goods_main_url
#                 get_goods_detail(goods_main_url, goods_id)
#             else:
#                 break
#     return begin_goods_main_url

# prev_goods_main_url = ''
# init_url = "http://www.huihui.cn/all?page="

# conn = pymongo.MongoClient('localhost', 27017)
# db = conn.sales
# goods_summarys = db.goods_summarys
# goods_contents = db.goods_contents

# while True:
#     for i in range(1, 2, 1):
#         url = "%s%s" % (init_url, i)
#         print "开始爬取:%s" % url
#         begin_goods_main_url = get_goods_info(url, prev_goods_main_url)
#         if begin_goods_main_url:
#             prev_goods_main_url = begin_goods_main_url
#             print prev_goods_main_url
#             break
#     print "等待下一次爬取，休息10分钟"
#     time.sleep(600)
