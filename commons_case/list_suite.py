# -*- coding: utf-8 -*-
list_a = ['share.huoshan.com', 'www.baidu.com']
a_url = 'baidu.com'
if any(a_url in item for item in list_a):
    print(111)
