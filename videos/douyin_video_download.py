import json
import os
import re
from typing import Tuple

import requests


class DouyinDownloader:
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }

    def __init__(self, url: str, save_folder: str):
        self.url = url
        self.save_folder = save_folder
        self.title = ''  # type: str
        self.video_url = ''

    def get_video_url_and_title(self):
        r = requests.get(url=self._find_link(self.url)[0])
        key = re.findall('video/(\d+)?', str(r.url))[0]
        jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'  # 官方接口
        js = json.loads(requests.get(url=jx_url, headers=self.headers).text)
        try:
            video_url = str(js['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm', 'play')  # 去水印后链接
        except Exception:
            print('视频链接获取失败')
            video_url = ''
        self.video_url = video_url
        # try:
        #     music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
        # except Exception:
        #     print('该音频目前不可用')
        #     music_url = ''
        try:
            video_title = str(js['item_list'][0]['desc'])
            music_title = str(js['item_list'][0]['music']['author'])
        except Exception:
            print('标题获取失败')
            video_title = '视频走丢啦~'
            music_title = '音频走丢啦~'
        self.title = video_title
        return self.video_url, self.title
        # return self._download(video_url, music_url, video_title, music_title)

    def download(self):
        r = requests.get(url=self._find_link(self.url)[0])
        key = re.findall('video/(\d+)?', str(r.url))[0]
        jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'  # 官方接口
        js = json.loads(requests.get(url=jx_url, headers=self.headers).text)
        try:
            video_url = str(js['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm', 'play')  # 去水印后链接
        except Exception:
            print('视频链接获取失败')
            video_url = ''
        try:
            music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
        except Exception:
            print('该音频目前不可用')
            music_url = ''
        try:
            video_title = str(js['item_list'][0]['desc'])
            music_title = str(js['item_list'][0]['music']['author'])
        except Exception:
            print('标题获取失败')
            video_title = '视频走丢啦~'
            music_title = '音频走丢啦~'
        # return self._download(video_url, music_url, video_title, music_title)
        print(video_url, music_url, video_title, music_title)

    @staticmethod
    def _find_link(text: str):
        # findall() 查找匹配正则表达式的字符串
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        return url


if __name__ == "__main__":
    d = DouyinDownloader(url='https://v.douyin.com/8qUmuyJ/', save_folder='./test/')
    d.download()
    # urlarg, musicarg = main()
    # video_download(urlarg, musicarg)
