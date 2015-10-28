# -*- coding: utf-8 -*-
import top.api

url = "https://item.taobao.com/item.htm?spm=5706.1529727.a31f1.2.K22uPH&scm=1007.10977.6259.100200300000000&id=19975899149&pvid=dc4b367a-c614-431c-85de-5c462ebea5e1"
req = top.api.TbkItemsConvertRequest(url, port)
req.set_app_info(top.appinfo(appkey, secret))

req.track_iids = "value1,value2,value3"
req.fields = "click_url"
req.nick = "hz0799"
req.outer_code = "bbs"
req.num_iids = "1,2,3"
req.pid = 123456
req.refer_type = 1
try:
    resp = req.getResponse()
    print(resp)
except Exception, e:
    print(e)
