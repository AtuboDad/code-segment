# -*- coding: utf-8 -*-
import re
import requests
from time import sleep

url = 'https://www.cfstc.org/bzgk/gk?action=yulanPDF&s_file_id=1787'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'JSESSIONID=0000IuK8nWZYRray54fFXLuiyBh:1bk8l9fqi',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

leng = 1
filename = r'D:\workspaces\pythonspaces\QT_downloader\simulation\commons_case\test.pdf'
torrent = requests.get(url, headers=headers, stream=True, verify=False)
# print(torrent.content)
with open(filename, 'wb') as f:
    f.write(torrent.content)
    f.flush()


