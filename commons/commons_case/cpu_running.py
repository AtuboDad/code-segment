# -*- coding: utf-8 -*-
import time
import argparse
from multiprocessing import Process
from multiprocessing import cpu_count
import math
import random


def exec_func(bt):
    time.sleep(bt)


if __name__ == "__main__":

    parse = argparse.ArgumentParser(description='runing')

    parse.add_argument(
        "-c",
        "--count",
        default=cpu_count(),
        help='cpu count'
    )

    parse.add_argument(
        "-t",
        "--time",
        default=1,
        help='cpu time'
    )

    args = parse.parse_args()

    # cpu_logical_count = int(args.count)
    cpu_logical_count = 5

    cpu_sleep_time = args.time

    try:
        cpu_sleep_time = int(args.time)
    except ValueError:
        try:
            cpu_sleep_time = float(args.time)
        except ValueError as ex:
            raise ValueError(ex)

    print('====================占用CPU核数{}.===================='.format(cpu_logical_count))
    print('资源浪费starting......')
    print('cpu_sleep_time: {}'.format(cpu_sleep_time))

    try:

        ps_list = []
        # p = Process(target=exec_func, args=("bt",))

        while True:

            now_localtime = time.strftime("%H:%M:%S", time.localtime())
            if "09:00:00" < now_localtime < "19:00:00":
                run_core = random.randint(0, 7)
                for i in range(0, run_core):
                    process = Process(target=exec_func, args=(cpu_sleep_time,))
                    ps_list.append(process)
                    process.start()

                for ps_item in ps_list:
                    ps_item.join()
            else:
                time.sleep(60)
    except KeyboardInterrupt:
        print("手工结束!")
