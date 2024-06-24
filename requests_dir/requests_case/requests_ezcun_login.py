# -*- coding: utf-8 -*-
import time
import requests
import functools
import pickle
import os
import json

from lxml import etree

from simulation.playwright_case.common_logger import logger

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'Accept': '*/*'}


class EzcunSession:

    def __init__(self):
        self.cookies_dir_path = "../playwright_case/cookies/"
        self.user_agent = user_agent
        self.session = self._init_session()

    def _init_session(self):
        session = requests.session()
        session.headers = self.get_headers()
        return session

    def get_headers(self):
        return {"User-Agent": self.user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;"
                          "q=0.9,image/webp,image/apng,*/*;"
                          "q=0.8,application/signed-exchange;"
                          "v=b3",
                "Connection": "keep-alive"}

    def get_session(self):
        return self.session

    def set_cookies(self, cookies):
        self.session.cookies.update(cookies)

    def get_cookies(self):
        return self.get_session().cookies


    def load_cookies_from_local(self):
        cookies_file = ''

        if not os.path.exists(self.cookies_dir_path):
            return False
        for name in os.listdir(self.cookies_dir_path):
            if name.endswith('.cookies'):
                cookies_file = '{}{}'.format(self.cookies_dir_path, name)
                break

        if cookies_file == '':
            return False

        with open(cookies_file, 'rb') as f:
            load_cookies = pickle.load(f)
        self.set_cookies(load_cookies)


    def save_cookies_to_local(self, cookie_file_name):
        """
        保存Cookie到本地
        :param cookie_file_name: 存放Cookie的文件名称
        :return:
        """
        cookies_file = '{}{}.cookies'.format(self.cookies_dir_path, cookie_file_name)
        directory = os.path.dirname(cookies_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(cookies_file, 'wb') as f:
            pickle.dump(self.get_cookies(), f)


class CommonLogin:

    def __init__(self, spider_session: EzcunSession):
        self.spider_session = spider_session

        self.session = self.spider_session.get_session()

        self.is_login = False
        self.refresh_login_status()

    def refresh_login_status(self):
        """
        刷新是否登录状态
        :return:
        """
        self.is_login = self._validate_cookies()

    def _validate_cookies(self):
        """
        验证cookies是否有效（是否登陆）
        通过访问用户订单列表页进行判断：若未登录，将会重定向到登陆页面。
        :return: cookies是否有效 True/False
        """
        url = 'https://ezcun.egongzheng.com/webEvidence/webInterception.do'
        payload = {
            'rid': str(int(time.time() * 1000)),
        }
        try:
            resp = self.session.get(url=url, params=payload, allow_redirects=False)
            if not resp.text.find('onclick="login()"') > -1:
                return True
        except Exception as e:
            logger.error("验证cookies是否有效发生异常", e)
        return False

    def _get_login_page(self):
        """
        获取PC端登录页面
        :return:
        """
        url = "https://ezcun.egongzheng.com/"
        page = self.session.get(url, headers=self.spider_session.get_headers())
        return page

    def _login(self):
        ezcun_login_url = 'https://ezcun.egongzheng.com/login/ajax/login.do'
        req_data = {
            'loginName': '13625962371',
            'passWord': 'woxihuanni1314',
            'code': '',
            'userType': 2,
            'remember': 'false',
        }

        response = self.session.post(ezcun_login_url, data=req_data, headers=headers)
        print('登录返回信息： ', response.content)

    def sign_up(self):
        self._get_login_page()

        self._login()

        self.refresh_login_status()



class EzcunSpider:

    def __init__(self):
        self.spider_session = EzcunSession()

        self.spider_session.load_cookies_from_local()

        self.qrlogin = CommonLogin(self.spider_session)

        self.session = self.spider_session.get_session()


    def sign_up(self):
        if self.qrlogin.is_login:
            logger.info('已经登录成功')
            return

        print('需要登录')
        self.qrlogin.sign_up()

        if self.qrlogin.is_login:
            self.spider_session.save_cookies_to_local('13625962371')
        else:
            print("登录失败！")


    def check_login(func):
        @functools.wraps(func)
        def new_func(self, *_args, **_kwargs):
            if not self.qrlogin.is_login:
                logger.info("{0} 需登登陆".format(func.__name__))
                self.sign_up()
            return func(self, *_args, **_kwargs)
        return new_func


    def _execute(self):
        response = self.session.post('https://ezcun.egongzheng.com/webEvidence/v_dataStorage.do')
        text = response.text
        print('请求网页取证页面返回: ', text)
        result_data = json.loads(text)
        evidence_list = []
        if len(result_data['resultData']['evid']) > 0:
            print(result_data['resultDesc'])
            print(result_data['resultData']['orgName'])

            for item in result_data['resultData']['evid']:
                evidence_item = {
                    'orgName': item['orgName'],
                    'userRealName': item['userRealName'],
                    'evidId': item['evidId'],
                    'orgId': item['orgId'],
                    'evidCreateTime': item['evidCreateTime'],
                    'createTime': item['createTime'],
                    'storageNo': item['storageNo'],
                    'requestUrl': item['requestUrl'],
                    'loginName': item['loginName'],
                    'evidStatus': item['evidStatus'],
                    'validDays': item['validDays'],
                    'evidName': item['evidName'],
                }
                evidence_list.append(evidence_item)
                print(evidence_item)

    @check_login
    def execute(self):
        self._execute()

def main():
    ezcun_spider = EzcunSpider()
    ezcun_spider.execute()

if __name__ == '__main__':
    main()

