# -*- coding: utf-8 -*-
import asyncio
import time


@asyncio.coroutine
def tailf():
    try:
        create = asyncio.create_subprocess_exec(
            'python', '-V',
            stdout=asyncio.subprocess.PIPE,
        )
        proc = yield from create

        while True:
            l = yield from proc.stdout.readline()
            print(l)

    except Exception as e:
        print('CAUGHT', type(e))
        raise e


@asyncio.coroutine
def task():
    yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()
tailf_task = loop.create_task(tailf())
loop.run_until_complete(asyncio.wait([task()]))
tailf_task.cancel()
loop.run_until_complete(asyncio.wait([tailf_task]))
loop.close()
