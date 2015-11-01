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


class Zhizhizhi_spider(object):

    """docstring for ClassName"""

    def __init__(self):

        self.domain = 'http://zhizhizhi.com/'
        self.source = 'zhizhizhi'
        self.source_name = '值值值'
        self.tool = qiniu_tool.Tool()
        self.baseinfo = baseinfo.Baseinfo()
        self.goods_summarys = self.baseinfo.db.goods_summarys
        self.goods_contents = self.baseinfo.db.goods_contents
        self.init_url_str = "http://zhizhizhi.com/page/"
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
        content_div = soup.find("div", "content_all")
        title = content_div.find("span", "otitle").string.encode('utf8').strip()
        sub_title = content_div.find("span", "dprice").string.encode('utf8').strip()
        pattern = 'link-yh-\d+'
        goods_url_ori = self.domain + re.findall(pattern, content_div.find("div", "tit_bar_fr").find("a")['href'])[0]
        goods_url_page = requests.get(goods_url_ori)
        goods_url = goods_url_page.url
        content_main_div = content_div.find_all("div", "content_a")
        content_main = ""
        for item in self.update_url(content_main_div):
            content_main += str(item)
        goods_content = {'title': title, 'sub_title': sub_title, 'goods_url': goods_url,
                         'content_main': content_main, 'goods_id': goods_id}
        self.goods_contents.insert_one(goods_content)

    def get_goods_summary_title(self, tag):
        goods_title = tag.find('span', 'otitle').string.encode('utf8').strip()
        skip_str_list = ["置顶", "值值值"]
        for skip_str in skip_str_list:
            if skip_str in goods_title:
                goods_title = None
                break
        return goods_title

    def get_goods_info(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")
        content_div = soup.find_all("div", "post_box")
        i = 0
        for item in content_div:
            goods_url_tag = item.find("a", href=re.compile('http://zhizhizhi.com/p/\d+/'))
            goods_title = self.get_goods_summary_title(item)
            if goods_title is None:
                continue
            if goods_url_tag:
                i += 1
                passdue_tag = 0
                shop_name = item.find("li", "theshop").find('a').string.encode('utf8').strip()
                goods_type = item.find("div", "other_box").find('a').string.encode('utf8').strip()
                goods_main_url = goods_url_tag['href']
                goods_id = str(hash(goods_main_url))
                goods_ico = self.tool.get_pic(item.find("div", "post_box_lr").find('img')['src'])
                goods_content = item.find("div", "text").contents[0].encode('utf8').strip()
                goods_sub_title = item.find('span', 'dprice').string.encode('utf8').strip()
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
                    self.baseinfo.get_goods_shop(shop_name)
                else:
                    break
        self.baseinfo.update_goods_last_spider_logs(
            self.source, i, begin_goods_main_url)
        self.baseinfo.update_goods_count(self.source, i-1)
        return begin_goods_main_url


while True:
    zhizhizhi = Zhizhizhi_spider()
    for i in range(1, 2, 1):
        url = "%s%s/" % (zhizhizhi.init_url_str, i)
        print "开始爬取:%s" % url
        begin_goods_main_url = zhizhizhi.get_goods_info(url)
        if begin_goods_main_url:
            break
    print "等待下一次爬取，休息10分钟"
    time.sleep(600)
