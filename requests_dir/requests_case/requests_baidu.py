# -*- coding: utf-8 -*-
import json
import win32api
import time
import requests
from playwright.sync_api import sync_playwright


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'Accept': '*/*'}

def main():
    win32api.ShellExecute(0, 'open', 'C:\\Google\\Chrome\\Application\\chrome.exe', '--remote-debugging-port=9222', '', 1)
    time.sleep(2)
    url = 'http://127.0.0.1:9222/json/version'
    response = requests.get(url, data=None, headers=headers)
    result_text = json.loads(response.text)
    web_socket_debugger_url = result_text['webSocketDebuggerUrl']

    playwright = sync_playwright().start()
    browser = playwright.chromium.connect_over_cdp(endpoint_url=web_socket_debugger_url)
    browser_context = browser.new_context(accept_downloads=True)

    page = browser_context.new_page()

    # Click download button
    with page.expect_download() as download_info:
        page.goto("https://www.runoob.com/try/try.php?filename=tryhtml5_a_download")
        page.frame(name="iframeResult").click('img[alt="runoob.com"]')
    download = download_info.value
    # 等待下载完成，path为下载文件的存储路径，执行context.close()之后，下载的文件会被删除
    # path = download.path()
    download.save_as(r'./test.png')
    time.sleep(2)
    browser_context.close()


if __name__ == '__main__':
    # 获取数据
    main()
