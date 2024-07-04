#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import base64,hmac
import urllib.parse
import urllib.request
import time
import json



class DingDingWebHook(object):
    def __init__(self, secret=None, url=None):
        """
        :param secret: 安全设置的加签秘钥
        :param url: 机器人没有加签的WebHook_url
        """
        if secret is not None:
            secret = secret
        else:
            secret = 'SEC45fc71c76792effb8044e5be29311ba94c33144c6487fd75c11702be457cd052'  # 加签秘钥 正式

        if url is not None:
            url = url
        else:
            url = "https://oapi.dingtalk.com/robot/send?access_token=fdfadf0f87035cc11038c7fd3fbc3bab9a0d380c1691b324aa075bd5d86015cd"  # 无加密的url # 正式

        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        """

        timestamp = str(round(time.time()) * 1000)  # 时间戳
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))  # 最终签名

        self.webhook_url = url + '&timestamp={}&sign={}'.format(timestamp, sign)  # 最终url，urls+时间戳+签名

    def send_meassage(self, data):
        """
        发送消息至机器人对应的群
        :param data: 发送的内容
        :return:
        """
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        send_data = json.dumps(data)  # 将字典类型数据转化为json格式
        send_data = send_data.encode("utf-8")  # 编码为UTF-8格式
        request = urllib.request.Request(url=self.webhook_url, data=send_data, headers=header)  # 发送请求
        # print(self.webhook_url)
        opener = urllib.request.urlopen(request)  # 将请求发回的数据构建成为文件格式
        # print(opener.read())  # 打印返回的结果



if __name__ == '__main__':
    my_secret = "SEC2226a3c1b93acb608b71c410991ac034ca021370d4cbfa353fcf3c003871e7ab"
    my_url = "https://oapi.dingtalk.com/robot/send?access_token=d6d6aa1af8b09de44933ad15ba9f1ec2da49cf3f0779ddd822e0c22c6c7f9a87"

    my_data = {
        "msgtype": "markdown",
        "markdown": {"title": "",
                     "text": "## 系统发布 \n> "
                             "\n- **当前北京时间: 2022-12-15 00:00:00**"
                             "\n- 402"},
        "at": {
            "atUserIds": "",
            "isAtAll": True}  # 是否@所有人
    }
    vt_name = "test"  # 漏洞名称
    affect_url = "s"
    severity_level = "s"
    last_seen_1 = "s"
    affects_detail = "s"
    my_data["markdown"]["title"] = vt_name
    my_data["markdown"][
        "text"] = "## %s \n>  \n- **1: %s** \n- **2: %s**  \n- **3: %s** \n- **4: %s** \n- **描述: %s** " % (
        vt_name, vt_name, affect_url, severity_level, last_seen_1, affects_detail
    )
    dingding = DingDingWebHook(secret=my_secret, url=my_url)
    dingding.send_meassage(my_data)