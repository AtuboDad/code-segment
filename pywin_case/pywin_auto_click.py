# -*- coding: utf-8 -*-
import os
import random
import datetime
import traceback
import pyautogui
import time
import win32api
import win32con
import win32gui
import win32clipboard as w

from playwright.sync_api import sync_playwright
from queue import Queue


success_code = 1000  # 正确状态
video_error = 1001  # video错误
video_not_exist = 1002  # video not exist
file_not_exist_code = 2000
novel_not_exist = 2001
novel_author_not_match = 2002
novel_title_not_match = 2003
file_not_exist = 3000
notifyEventStart = 10000

notifyEventTypeItem = 10
notifyEventTypeAll = 20
notifyEventTypeFile = 30

# 设置和粘贴剪贴板
def ClipboardText(ClipboardText):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, ClipboardText)
    w.CloseClipboard()
    time.sleep(1)
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟发送动作
def SendMsg():
    # win32api.keybd_event(18, 0, 0, 0)
    # win32api.keybd_event(83, 0, 0, 0)
    # win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟发送微信消息
def SendWxMsg(wxid, sendtext, x, y):
    # 先启动微信
    chatroom = '微信'
    win = win32gui.FindWindow('WeChatMainWndForPC', chatroom)
    print("找到窗口句柄：%x" % win)
    if win != 0:
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.SetActiveWindow(win)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 0, 0, 300, 500, win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(1)
        tit = win32gui.GetWindowText(win)
        print('已启动【' + str(tit) + '】窗口')
        time.sleep(1)
    else:
        print('找不到【%s】窗口' % chatroom)
        exit()

    time.sleep(1)
    # 定位到搜索框
    pyautogui.moveTo(143, 39)
    pyautogui.click()
    # 搜索窗口
    ClipboardText(wxid)
    time.sleep(1)
    # 进入窗口
    pyautogui.moveTo(155, 120)
    pyautogui.click()
    # 粘贴文本内容
    ClipboardText(sendtext)
    SendMsg()
    print('已发送')
    time.sleep(1)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    # 最小化
    win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
    time.sleep(1)

    win_web = win32gui.FindWindow('CefWebViewWnd', chatroom)
    win32gui.ShowWindow(win_web, win32con.SW_SHOWMAXIMIZED)
    win32gui.SetActiveWindow(win_web)
    win32gui.ShowWindow(win_web, win32con.SW_SHOW)
    time.sleep(4)

    win32gui.ShowWindow(win_web, win32con.SW_SHOWMINIMIZED)
    time.sleep(2)


def read_file(file_path):
    if not os.path.exists(file_path):
        return ''

    with open(file_path, 'r') as f:
        line = f.readline()
        print(line)
        return line


class ScreenShotExecutor:
    def __init__(self, chrome_path, send_q, proxy_type, file_path):
        self.shot_flag = ''
        self.shot_height = 0
        self.start_flag = 0
        self.start_index = 1
        self.current_time = ''
        self.__dirname = os.getcwd()
        self.startDate = ''
        self.timeout_mill_seconds = 60000
        self.max_height_limit = 20000
        self.result_data = {}
        self.url_lines = []

        self.needReplaceChars = ['|', '“', '”', '\/', '\\\\', '*', '?', '？', '<', '>', ':', '：', ' ', '　', '^']
        self.UserAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'

        self.default_encoding = 'utf-8'
        self.osLineSeparator = '\r\n'
        self.osFileSeparator = '\\'
        self.failedUrls = []

        self.chrome_path = chrome_path
        self.sync_playwright_work = None
        self.browser = None
        self.browser_context = None
        self.page = None
        self.send_q = send_q
        self.proxy_type = proxy_type
        self.file_path = file_path
        self.headless = True
        self.page_start_time = None

    def init(self, use_local_dir=False):
        # args = ['--no-sandbox', '--disable-infobars', '--lang=zh-CN', '--window-size=1920,969', '--start-maximized', '--window-position=0,0']
        args = ['--no-sandbox', '--disable-infobars', '--lang=zh-CN', '--start-maximized', '--window-position=0,0']
        ignore_default_args = ['--enable-automation']

        self.sync_playwright_work = sync_playwright().start()
        if use_local_dir:
            self.browser = self.sync_playwright_work.chromium.launch_persistent_context(user_data_dir='D:/home/chrome/', executable_path=self.chrome_path,
                                                                                        args=args,
                                                                                        ignore_default_args=ignore_default_args,
                                                                                        headless=self.headless)
            self.browser_context = self.browser
            self.page = self.browser_context.new_page()
        else:
            self.browser = self.sync_playwright_work.chromium.launch(executable_path=self.chrome_path,
                                                                     args=args,
                                                                     ignore_default_args=ignore_default_args,
                                                                     headless=self.headless)
            self.browser_context = self.browser.new_context()
            self.page = self.browser_context.new_page()
        self.page.set_viewport_size({'width': 1910, 'height': 950})
        self.page_start_time = time.time()

    # 递归创建目录 同步方法
    @staticmethod
    def dirs_make(dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return True

    @staticmethod
    def handle_dialog(dialog):
        dialog.dismiss()

    def replace_chars(self, title):
        for i in range(len(self.needReplaceChars)):
            need_replace_char = self.needReplaceChars[i]
            char_index = title.find(need_replace_char)
            while char_index >= 0:
                title = title.replace(need_replace_char, '')
                char_index = title.find(need_replace_char)
        return title

    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_file_prefix(date_format='%Y%m%d%H%M%S'):
        return datetime.datetime.now().strftime(date_format)

    @staticmethod
    def get_current_date():
        return datetime.datetime.now().strftime('%Y-%m-%d')

    def main_run(self, request_url, id_=None, shot_height=None):

        execute_result = {'result_flag': False}
        page_start_time = time.time()

        try:
            self.page.goto(request_url, timeout=self.timeout_mill_seconds)
            self.page.wait_for_timeout(3000)

            height_limit = False
            scroll_times = 0
            m_values = {'scrollEnable': True, 'height_limit': height_limit, 'times': 10}
            while m_values['scrollEnable']:
                m_values = self.page.evaluate('''([height_limit, page_screentshot_height_limit]) => {
                            let times = 1;
                            let scrollEnable = true;
                            let innerHeight = window.innerHeight;
                            let divHeight = 0;
                            if (undefined !== document.body && null != document.body) {
                              window.scrollBy(0, innerHeight);
                              let h = document.body.clientHeight;
                              times = parseInt(h / innerHeight);
                              divHeight = h;
                              if (document.body.clientHeight > page_screentshot_height_limit) {
                                height_limit = true;
                              }
                            } else {
                              scrollEnable = false;
                            }
                            times = times + 1;
                            return {
                              'scrollEnable': scrollEnable,
                              'height_limit': height_limit,
                              'times': times,
                              'divHeight': divHeight
                            };
                        }''', [height_limit, self.max_height_limit])

                random_mill_second = random.randint(2000, 5000)
                self.page.wait_for_timeout(random_mill_second)

                scroll_times = scroll_times + 1
                print('本地- ' + request_url + ' 需要滚动 : ' + str(m_values['times']) + '次 , 滚动第[' + str(scroll_times) + ']次')
                if scroll_times > m_values['times']:
                    print(request_url + ' 结束')
                    m_values['scrollEnable'] = False

            self.page.wait_for_timeout(4000)
            end_time = time.time()
            print('本地-请求目标地址以及屏幕滚动耗时(单位毫秒:ms) :' + str(end_time - page_start_time) + ' , ' + request_url)

            parent_file_path = os.getcwd() + self.osFileSeparator + 'local_images' + self.osFileSeparator

            title = self.page.title()
            title = self.replace_chars(title)

            # 文件名称
            time_file_name = self.get_file_prefix('%Y%m%d')
            page_file_name = time_file_name + self.osFileSeparator + title + '.jpg'
            page_pdf_file_name = parent_file_path + time_file_name + self.osFileSeparator + title + '.pdf'
            page_file_path = parent_file_path + page_file_name
            if not os.path.exists(parent_file_path + time_file_name):
                self.dirs_make(parent_file_path + time_file_name)

            # 生成图片, 全页面
            try:
                result_code = self.page.screenshot(path=page_file_path, full_page=True)
                if m_values['height_limit']:
                    self.page.pdf(path=page_pdf_file_name,
                                  format='A4',
                                  print_background=True,
                                  display_header_footer=True,
                                  page_ranges=""
                                  )
                self.page.wait_for_timeout(2000)
            except Exception as e:
                err_info = str(traceback.format_exc())
                print(err_info)
                result_code = file_not_exist_code
            if result_code == file_not_exist_code:
                current_time = self.get_current_time()
                print("生成截图失败.")
                return execute_result

        except Exception as e:
            err_info = str(traceback.format_exc())
            print(err_info)
            print('本地-执行异常: ', str(e))

        return execute_result

    def close_browser(self):
        try:
            self.page.wait_for_timeout(5000)
            self.page.close()
            page_end_time = time.time()
            print('本地-页面加载到结束共耗时(单位毫秒:ms) :' + str(page_end_time - self.page_start_time))

            self.browser.close()
            self.sync_playwright_work.stop()
        except:
            pass


if __name__ == '__main__':
    x, y = pyautogui.position()
    print(x, y)

    # 调用函数（微信号或微信昵称或备注，需要发送的文本消息）
    # time.sleep(10)
    # param_file_path = r'D:/test.txt'
    # content = read_file(param_file_path)
    # if content and len(content) > 0:
    x = 464
    y = 245

    # content = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5NzQ0NTg0MA==&scene=124#wechat_redirect'
    # SendWxMsg('文件传输助手', content, x, y)
    # content = 'https://mp.weixin.qq.com/mp/getverifyinfo?__biz=MjM5NzQ0NTg0MA=='
    # SendWxMsg('文件传输助手', content, x, y)
    # content = 'https://mp.weixin.qq.com/s?__biz=MjM5NzQ0NTg0MA==&mid=2653596185&idx=1&sn=62de619b067c7e0b88a37a028ec4471f&'
    # SendWxMsg('文件传输助手', content, x, y)

    executable_path = "C:\\Google\\Chrome\\Application\\chrome.exe"
    script_send_queue = Queue()
    proxy_type = None
    file_path = './test-web.txt'
    executor = ScreenShotExecutor(executable_path, script_send_queue, proxy_type, file_path)
    executor.init()
    executor.main_run('https://weibo.com/5624116865/about')
    executor.main_run('http://weibo.com/5624116865/DkoQji3UC')
    executor.main_run('http://shenghuo.b2b168.com/s168-123276417.html')
    executor.main_run('https://mp.weixin.qq.com/s?__biz=MjM5NzQ0NTg0MA==&mid=2653596185&idx=1&sn=62de619b067c7e0b88a37a028ec4471f&')
    executor.close_browser()
