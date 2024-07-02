# -*- coding: utf-8 -*-
from pyppeteer.launcher import launch
from pyppeteer_stealth import stealth
import asyncio

from Commons import status_codes, progress_infos

def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def start_browser(start_params):
    try:
        browser = await launch(
            {'headless': False,
             'executablePath': 'C:\\Google\\Chrome\\Application\\chrome.exe',
             'args': ['--no-sandbox', '--disable-infobars', '--lang=zh-CN', '--start-maximized'],
             },
            args=['--window-size=1920,1080'],
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
        )
        width, height = screen_size()
        page = await browser.newPage()
        progress_infos.progress_info_1 = 10
        await stealth(page)
        await page.waitFor(2000)
        progress_infos.progress_info_1 = 12
        await page.evaluateOnNewDocument('''
                            Modernizr.hairline = true
                        ''')
        await page.setViewport(viewport={"width": width, "height": height})
        progress_infos.progress_info_1 = 20
        await page.goto(start_params.start_url)
        progress_infos.progress_info_1 = 40
        await page.waitFor(6000)
        progress_infos.progress_info_1 = 50
        await page.screenshot({'path': 'example.png', 'fullPage': True})
        progress_infos.progress_info_1 = 80
        await browser.close()
        progress_infos.progress_info_1 = 100
        status_codes.start_flag = False
        return {'status': 'success', 'msg': '成功'}
    except Exception as e:
        print(e)


def do_start(start_params):
    progress_infos.progress_info_1 = 1
    loop1 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop1)
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(start_browser(start_params))
