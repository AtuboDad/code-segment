# -*- coding: utf-8 -*-
import json
import win32api
import time
import requests
from playwright.sync_api import sync_playwright


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
           'Accept': '*/*',
           'cookie': 'cna=xWc4GnuPb1wCARua6/L/gxkl; cdpid=W8CN6CD03kce; yunpk=1676252676330615; cnaui=2211413855530; aui=2211413855530; sca=233a9719; tbsa=13dcc08b11eb50e0cdd3d848_1646700955_2; atpsida=a8dbf1e045eb0351111dc4a5_1646704807_34',
           }

def main():
    # down_data = {"spm": "a2o4z.0pages0contract0download0html.0.0.209d26f7idwhUW",
    #              "Expires": 1677808805,
    #              "OSSAccessKeyId": "TMP.3KhvetoxHaRcLi7mt91PXctJzqUMh99Nk9mc1ZxaKVDiEFVtbPcKUuzsG4tssjak5694h72L628frzkzQiVhuhvigzTKEL",
    #              "Signature": "1K9/f7DhwXYbsHdhEPyL2ge4xL4="
    #              }
    down_url = 'https://wdk-finance-settlement2.oss-cn-hangzhou.aliyuncs.com/settlement.path%3Dprod/finance-settlement/S202201222270505746-8371.xlsx?spm=a2o4z.0pages0contract0download0html.0.0.209d26f7idwhUW&Expires=1677808805&OSSAccessKeyId=TMP.3KhvetoxHaRcLi7mt91PXctJzqUMh99Nk9mc1ZxaKVDiEFVtbPcKUuzsG4tssjak5694h72L628frzkzQiVhuhvigzTKEL&Signature=1K9%2Ff7DhwXYbsHdhEPyL2ge4xL4%3D'
    down_res = requests.get(url=down_url, params={})

    with open('./test.xlsx', "wb") as code:
        code.write(down_res.content)

if __name__ == '__main__':
    # 获取数据
    main()
