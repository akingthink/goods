# -*- coding:utf-8 -*-

import concurrent.futures
import models
import os.path
import re
import subprocess
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

define("port", default=8000, help="run on the given port", type=int)


class Goods_summarys_handler(tornado.web.RequestHandler):

    def get(self, page=1):
        skip_cnt = (int(page) - 1) * 10
        goods_summarys = models.Goods_summarys.objects.skip(skip_cnt).limit(10)
        goods_last_updates = models.Goods_last_spider_logs.objects
        goods_counts = models.Goods_newest_spider_logs.objects
        goods_shops = models.Goods_shops.objects.limit(10)
        if not goods_summarys:
            self.redirect("/")
            return
        self.render("home.html", goods_summarys=goods_summarys,
                    goods_last_updates=goods_last_updates, goods_counts=goods_counts,
                    goods_shops=goods_shops)


class Goods_summarys_module(tornado.web.UIModule):

    """docstring for Goods_summarys_module"""

    def render(self, goods_summary):
        return self.render_string("modules/goods_summary.html", goods_summary=goods_summary)


class Goods_last_updates_module(tornado.web.UIModule):

    def render(self, goods_last_update):
        return self.render_string("modules/goods_last_update.html", goods_last_update=goods_last_update)


class Goods_counts_module(tornado.web.UIModule):

    def render(self, goods_count):
        return self.render_string("modules/goods_count.html", goods_count=goods_count)


class Goods_detail_handler(tornado.web.RequestHandler):

    """docstring for Goods_detail_handler"""

    def get(self, goods_id):
        goods_contents = models.Goods_contents.objects(goods_id=str(goods_id))
        goods_last_updates = models.Goods_last_spider_logs.objects
        goods_counts = models.Goods_newest_spider_logs.objects
        if not goods_contents:
            self.redirect("/")
            return
        self.render("goods_detail.html", goods_contents=goods_contents,
                    goods_last_updates=goods_last_updates, goods_counts=goods_counts)


class Goods_content_module(tornado.web.UIModule):

    """docstring for Goods_content_module"""

    def render(self, goods_content):
        return self.render_string("modules/goods_content.html", goods_content=goods_content)


class Goods_shops_module(tornado.web.UIModule):

    def render(self, goods_shop):
        return self.render_string("modules/shop_list.html", goods_shop=goods_shop)


class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r'/', Goods_summarys_handler),
            (r'/page=([^/]+)', Goods_summarys_handler),
            (r'/goods=([^/]+)', Goods_detail_handler),
        ]

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'ui_modules': {"Goods_summarys": Goods_summarys_module, "Goods_last_updates": Goods_last_updates_module,
                           "Goods_counts": Goods_counts_module, "Goods_content": Goods_content_module,
                           "Goods_shops": Goods_shops_module},
            'debug': True
        }

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
