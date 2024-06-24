# -*- coding: utf-8 -*-

import requests
import json


def main():
    notify_url = 'https://hwtest-notaryadmin.ezcun.com/api/orgadmin/third-callback/testify-attachment-pdf-generate/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8;'
    }
    data = {"status": 10000, "msg": "PDF合成成功", "data": {"total_page": 7, "sequence": "880456943947218944"}}
    params = json.dumps(data)
    response = requests.post(notify_url, data=params, headers=headers)
    if response and response.status_code == requests.codes.ok:
        print('回调成功', data['data']['sequence'])
    else:
        print('回调失败, 返回信息: ', response.text, data['data']['sequence'])


if __name__ == '__main__':
    # 获取数据
    main()
