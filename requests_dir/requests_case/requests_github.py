# -*- coding: utf-8 -*-
import requests


r = requests.get('https://api.github.com/user', auth=('AtuboDad', 'QWEqwe13!$'))
print(r.status_code)
print(r.headers['content-type'])
print(r.text)
print(r.json())