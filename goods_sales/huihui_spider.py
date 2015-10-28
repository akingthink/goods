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
import baseinfo


class Huiui_spider(object):

    """docstring for ClassName"""

    def __init__(self):

        self.domain = 'http://www.huihui.cn'
        self.source = 'huihui'
        self.source_name = '惠惠'
        self.tool = qiniu_tool.Tool()
        self.baseinfo = baseinfo.Baseinfo()
        self.goods_summarys = self.baseinfo.db.goods_summarys
        self.goods_contents = self.baseinfo.db.goods_contents
        self.init_url_str = "http://www.huihui.cn/all?page="
        self.prev_goods_main_url = self.baseinfo.get_prev_url(self.source)

    def has_data_log_but_no_class(self, tag):
        return tag.has_attr('data-log') and not tag.has_attr('class')

    def update_url(self, content_main_div):
        for item in content_main_div:
            img_tag = item.find("img")
            if img_tag:
                img_tag['src'] = self.tool.get_pic(img_tag['src'])
        return content_main_div

    def get_goods_detail(self, url, goods_id):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        content_div = soup.find("div", "hui-list")
        title = content_div.find("h1").find("a").string.encode('utf8').strip()
        sub_title = content_div.find("h4").string.encode('utf8').strip()
        pattern = '(^.*?)\?tag'
        if re.findall(pattern, content_div.find("h1").find("a")['href']):
            goods_url = re.findall(
                pattern, content_div.find("h1").find("a")['href'])[0]
        else:
            goods_url = content_div.find("h1").find("a")['href']
        content_main_div = content_div.find_all("div", "editor-mod")
        content_main = ""
        for item in self.update_url(content_main_div):
            content_main += str(item)
        goods_content = {'title': title, 'sub_title': sub_title, 'goods_url': goods_url,
                         'content_main': content_main, 'goods_id': goods_id}
        self.goods_contents.insert_one(goods_content)

    def get_goods_info(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        content_div = soup.find_all("div", "module-hui-list-item1")
        pattern = re.compile('\d+')
        i = 0
        for item in content_div:
            goods_url_tag = item.find("a", href=re.compile('/deals/\d+'))
            if goods_url_tag:
                i += 1
                passdue_tag = 0 if item.find(
                    "div", "hui-list-ctn passdue  clearfix") is None else 1
                shop_name = item.find("a", "shop").string.encode(
                    'utf8').strip() if item.find("a", "shop") is not None else '其他'
                goods_type = item.find(
                    "div", "list-shop").find(self.has_data_log_but_no_class).string.encode('utf8').strip()
                goods_main_url = self.domain + goods_url_tag['href']
                goods_id = str(hash(goods_main_url))
                goods_ico = self.tool.get_pic(item.find("img")['data-src'])
                goods_content = item.find(
                    "div", "hui-content-text").contents[1].contents[0].encode('utf8').strip()
                goods_title = item.find(
                    'div', 'hlist-list-text').find('h3').find('a').contents[0].encode('utf8').strip()
                goods_sub_title = item.find(
                    'div', 'hlist-list-text').find('h3').find('a').find('em').string.encode('utf8').strip()
                if i == 1:
                    begin_goods_main_url = goods_main_url
                if goods_main_url != self.prev_goods_main_url:
                    goods_summary = {'shop_name': shop_name, 'goods_type': goods_type,
                                     'goods_title': goods_title, 'goods_sub_title': goods_sub_title,
                                     'goods_main_url': goods_main_url, 'goods_ico': goods_ico,
                                     'goods_content': goods_content, 'passdue_tag': passdue_tag,
                                     'source': self.source, 'source_name': self.source_name,
                                     'goods_id': goods_id,
                                     'created_at': datetime.datetime.utcnow()}
                    self.goods_summarys.insert_one(goods_summary)
                    print goods_main_url
                    self.get_goods_detail(goods_main_url, goods_id)
                else:
                    break
        self.baseinfo.update_goods_last_spider_logs(
            self.source, i, begin_goods_main_url)
        self.baseinfo.update_goods_count(self.source, i)
        return begin_goods_main_url


while True:
    huihui = Huiui_spider()
    for i in range(1, 2, 1):
        url = "%s%s" % (huihui.init_url_str, i)
        print "开始爬取:%s" % url
        begin_goods_main_url = huihui.get_goods_info(url)
        if begin_goods_main_url:
            break
    print "等待下一次爬取，休息10分钟"
    time.sleep(600)
