# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd
import os

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar


def get_danmu(num1, num2, page):
    url = 'https://bullet-ws.hitv.com/bullet/2020/12/24/{}/{}/{}.json'
    danmu_url = url.format(num1, num2, page)
    response = requests.get(danmu_url)
    response.encoding = 'utf-8'
    jsons = json.loads(response.text)
    details = []
    try:
        for i in range(len(jsons['data']['items'])):
            result = {}
            result['stype'] = num2
            result['id'] = jsons['data']['items'][i]['id']
            try:
                result['uname'] = jsons['data']['items'][i]['uname']
            except:
                result['uname'] = ''
            result['content'] = jsons['data']['items'][i]['content']
            result['time'] = jsons['data']['items'][i]['time']
            try:
                result['v2_up_count'] = jsons['data']['items'][i]['v2_up_count']
            except:
                result['v2_up_count'] = ''
            details.append(result)
    except TypeError:
        return details
    return details


# 输入关键信息
def count_danmu(page_num):
    danmu_total = []
    num1 = '021202'
    num2 = '10438285'
    page = page_num
    for i in range(page):
        danmu_total.extend(get_danmu(num1, num2, i))

    return danmu_total


def main():
    danmu_end = []
    # 获取1-32集
    for j in range(1, 33):
        danmu_end.extend(count_danmu(j))
        df = pd.DataFrame(danmu_end)
        # df.to_excel('danmu.xlsx')
        df.to_csv("bullet_data/第{}集.csv".format(j))
        danmu_end = []


def generate_bar():
    file_dir = 'bullet_data'

    keys = []
    values = []
    for i in range(1, 33):
        file_name = '第' + str(i) + '集'
        data_file = os.path.join(file_dir, file_name + '.csv')
        count = 0
        keys.append(file_name)
        with open(data_file, encoding='utf-8') as f:
            while True:
                buffer = f.read(1024 * 8192)
                if not buffer:
                    break
                count += buffer.count('\n')
            # print(data_file, count)
            values.append(count)

    c = (Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
         .add_xaxis(keys)
         .add_yaxis('弹幕数量', values)
         .set_global_opts(title_opts=opts.TitleOpts(title='装台', subtitle='芒果每集弹幕分布'), datazoom_opts=opts.DataZoomOpts())) \
        .render('芒果每集分布弹幕.html')


def rename_file():
    file_dir = 'bullet_data'
    for i in range(1, 33):
        src = file_dir + '/bullet' + str(i) + '.csv'
        dest = file_dir + '/第' + str(i) + '集.csv'
        os.rename(src, dest)


if __name__ == '__main__':
    # 获取数据
    # main()

    # 生成柱状图
    generate_bar()

    # 修改文件名称
    # rename_file()
