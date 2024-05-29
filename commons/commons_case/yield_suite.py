# -*- coding: utf-8 -*-
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield None
        if term is None:
            break
        total += term
        count += 1
        average = total / count
        return Result(count, average)

# 协程的触发
coro_avg = averager()
# 预激活协程
next(coro_avg)
try:
    coro_avg.send(None)
except StopIteration as exc: # 执行完成，会抛出StopIteration异常，返回值包含在异常的属性value里
    result = exc.value
    print(result)
