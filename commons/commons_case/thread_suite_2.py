# -*- coding: utf-8 -*-
from concurrent import futures


def do_run(info):
    for i in range(1000):
        print(info[i])

list_works = []

for i in range(5):
    list_works.append(('text%s' % i, 'info%s' % i))

with futures.ThreadPoolExecutor(2) as executor:
    executor.map(do_run, sorted(list_works))
