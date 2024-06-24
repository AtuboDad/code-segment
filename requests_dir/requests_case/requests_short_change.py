# -*- coding: utf-8 -*-
import requests


with open('./short_urls.txt') as f:
    while True:
        url = f.readline().strip('\n')
        if url:
            # print(url)
            res = requests.head(url)
            print(res.headers.get('location'))
        else:
            break