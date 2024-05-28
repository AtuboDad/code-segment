# -*- coding: utf-8 -*-
from concurrent import futures


def do_run(info):
    for i in range(1000):
        pass
    return info[0]

MAX_WORKS = 10
list_works = []

for i in range(5):
    list_works.append(('text%s' % i, 'info%s' % i))

workers = min(MAX_WORKS, len(list_works))

with futures.ThreadPoolExecutor(workers) as executor:
    results = executor.map(do_run, sorted(list_works))

for result in results:
    print(results)

print('=' * 20)

executor = futures.ThreadPoolExecutor(workers)
results = []
for idx, param in enumerate(list_works):
    result = executor.submit(do_run, param)
    results.append(result)
    print('result %s' % idx)

# 手动等待所有任务完成
executor.shutdown()
print('='*10)
for result in results:
    print(result.result())


print('*' * 20)