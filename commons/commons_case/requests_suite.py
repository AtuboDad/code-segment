# -*- coding: utf-8 -*-
import asyncio
import requests
from concurrent import futures
import json


def do_request(url):
    try:
        response = requests.get(url, timeout=2)
        if response.ok:
            return url, response.text
        else:
            return ''
    except Exception as e:
        # print(e)
        return ''


results = []
with futures.ThreadPoolExecutor(10) as executor:
    ports = [10000, 10188, 15000, 28317, 28511, 28521, 35500, 35600, 49152, 49153, 49156, 49155, 49194, 49554, 49590, 49589, 50777, 51105, 54321, 54530, 63342, 65358]
    for i in ports:
        url_item = 'http://127.0.0.1:%s/json' % str(i)
        # print(url_item)
        result = executor.submit(do_request, url_item)
        results.append(result)

for result in results:
    if str(result.result()) != '':
        print(str(result.result()))
