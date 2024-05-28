# -*- coding: utf-8 -*-
import win32print
import win32api
from datetime import datetime
import time
import re
from urllib import parse
from urllib.parse import urlsplit, SplitResult

import os

def method_1(num):
    try:
        if num == 1:
            with open(r'D:\workspaces\pythonspaces\QT_downloader\simulation\commons_case\asyncio_suite.py') as f:
                line = f.readline().strip('\n')
                print(line)
            return
    finally:
        print(1111)


# method_1(1)
str_a = '123.23.33.1:8994'
index = str_a.find(':')
print(index)
print(str_a[:index])
print(str_a[index + 1:])

time_ = datetime.strptime(str('2016.06.30'), '%Y.%m.%d')
print(time_)

f_time = time_.strftime("%Y.%m.%d")
print(f_time)

str_a = '1111 '
print(str_a)
print(str_a.strip())

print(287/30)

filename = r"D:\Documents\Downloads\rockyou.txt" #密码字典路径
filepath, tempfilename = os.path.split(filename)
print(filepath, tempfilename)
filepath, tempfilename = os.path.splitext(filename)

print(filepath, tempfilename)