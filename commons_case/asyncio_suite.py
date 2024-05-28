# -*- coding: utf-8 -*-
import asyncio

# import redis


async def task_run(num):
    print(num)
tasks = []
for i in range(10):
    task = task_run(i)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
