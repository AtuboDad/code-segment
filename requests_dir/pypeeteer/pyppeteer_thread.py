# -*- coding: utf-8 -*-
from PyQt5.QtCore import QThread, pyqtSignal
from pyppeteer.launcher import launch
from pyppeteer.page import Request
from pyppeteer_stealth import stealth
import asyncio

from Commons import status_codes, progress_infos

from Workers import pyppeteer_worker, requests_thread


class PyppeteerWorkThread(QThread):
    progress_bar = pyqtSignal()
    py_wt_pb = pyqtSignal(dict)

    def __init__(self):
        super(PyppeteerWorkThread, self).__init__()
        self.start_params = {}
        self.shot_mode = 0

    def define_params(self, start_params, mode):
        self.start_params = start_params
        self.shot_mode = mode

    def run(self):
        try:
            # loop1 = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop1)
            # loop = asyncio.get_event_loop()
            result_data = self.do_start(self.start_params, self.shot_mode)
            self.py_wt_pb.emit(result_data)
        # pyppeteer_worker.do_start(self.args)

        except Exception as e:
            print(e)

    def screen_size(self):
        """使用tkinter获取屏幕大小"""
        import tkinter
        tk = tkinter.Tk()
        width = tk.winfo_screenwidth()
        height = tk.winfo_screenheight()
        tk.quit()
        return width, height

    async def intercept(self, request):
        print(request.url)
        await request.abort()
        # if any(request.resourceType == _ for _ in ('stylesheet', 'image', 'font')):
        #     await request.abort()
        # else:
        #     await request.continue_()

    async def start_browser(self, start_params, shot_mode):
        try:
            browser = await launch(
                {'headless': False,
                 'executablePath': 'C:\\Google\\Chrome\\Application\\chrome.exe',
                 'args': ['--no-sandbox', '--disable-infobars', '--lang=zh-CN', '--start-maximized'],
                 'ignoreDefaultArgs': ["--enable-automation"],
                 },
                args=['--window-size=1920,1080'],
                handleSIGINT=False,
                handleSIGTERM=False,
                handleSIGHUP=False,
            )
            width, height = self.screen_size()
            print('width, height', width, height)
            page = await browser.newPage()
            progress_infos.progress_info_1 = 10
            self.progress_bar.emit()
            await stealth(page)
            # 注入js
            await page.evaluateOnNewDocument('''
            window.onload = function () {
            document.onmousedown = function (event) {
                var e = event || window.event || arguments.callee.caller.arguments[0];
                var obj = document.elementFromPoint(event.clientX, event.clientY);
                var objText = obj.innerText
                console.log(objText);
            };
            }
            ''')
            await page.waitFor(2000)
            progress_infos.progress_info_1 = 12
            self.progress_bar.emit()
            await page.setViewport(viewport={"width": width, "height": height})
            progress_infos.progress_info_1 = 20
            self.progress_bar.emit()
            await page.goto(start_params.start_url)
            progress_infos.progress_info_1 = 40
            self.progress_bar.emit()

            # 停留在当前页面
            await page.setRequestInterception(True)
            page.on('request', lambda req: self.intercept(req))

            await page.waitFor(2000)
            progress_infos.progress_info_1 = 50
            self.progress_bar.emit()

            if shot_mode > 1:
                if shot_mode == 3:
                    await page.screenshot({'path': 'example.png', 'fullPage': True})
                else:
                    await page.screenshot({'path': 'example.png'})

            progress_infos.progress_info_1 = 80
            self.progress_bar.emit()
            await browser.close()
            progress_infos.progress_info_1 = 100
            self.progress_bar.emit()
            status_codes.start_flag = False
            return {'status': 'success', 'msg': '成功'}
        except Exception as e:
            print(e)

    def do_start(self, start_params, shot_mode):
        progress_infos.progress_info_1 = 1
        self.progress_bar.emit()

        loop1 = asyncio.new_event_loop()
        asyncio.set_event_loop(loop1)
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.start_browser(start_params, shot_mode))
