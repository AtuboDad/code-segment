# -*- coding: utf-8 -*-
import re
import execjs
import requests
import hashlib
import json
from requests.utils import add_dict_to_cookiejar
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 关闭ssl验证提示
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
}
url = 'https://beian.miit.gov.cn/'
# 使用session保持会话
session = requests.session()


def run():
    # 第一次请求
    # response = session.get(url, headers=header, verify=False)
    # print('status1', response.status_code)
    #
    # # 提取js代码
    # js_clearance = re.findall('cookie=(.*?);location', response.text)[0]
    # # 执行后获得cookie参数js_clearance
    # result = execjs.eval(js_clearance).split(';')[0]
    # # 添加cookie
    # add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': result})
    # # 第二次请求
    # resp = session.get(url, cookies=session.cookies)
    # js_clearance = re.findall('cookie=(.*?);location', response.text)[0]
    # print('js_clearance', execjs.eval(js_clearance))
    # result = execjs.eval(js_clearance).split(';')[0]
    # # 提取参数并转字典
    # print('result', resp.text)
    # print('status2', resp.status_code)

    text = ''
    go = json.loads(re.findall(r'};go\((.*?)\)</script>', resp.text)[0])

    for i in range(len(go['chars'])):

        for j in range(len(go['chars'])):

            vales = go['bts'][0] + go['chars'][i] + go['chars'][j] + go['bts'][1]

            if go['ha'] == 'md5':
                ha = hashlib.md5(vales.encode()).hexdigest()
            elif go['ha'] == 'sha1':
                ha = hashlib.sha1(vales.encode()).hexdigest()
            elif go['ha'] == 'sha256':
                ha = hashlib.sha256(vales.encode()).hexdigest()
            if ha == go['ct']:
                __jsl_clearance_s = vales


run()
