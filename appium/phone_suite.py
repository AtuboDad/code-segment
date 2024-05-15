# -*- coding: utf-8 -*-

from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# pywinauto PC端，微信自动化
class TestDemo:

    def __init__(self):
        self.driver = None
        self.desire_cap = {
            "platformName": "Android",  # 操作系统
            "deviceName": "c53f0c08",  # 设备 ID
            # "appPackage": "com.sina.weibo",
            # "appActivity": "com.sina.weibo.MainTabActivity",
            "appPackage": "com.tencent.mm",
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            # "appActivity": "com.tencent.mm.plugin.webview.ui.tools.WebViewUI",
            "noReset": True,
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:tools'
            }
        }

        # com.tencent.mm:tools

        self.setup()

    def setup(self):

        # androidProcess：webview是独立进程的，导致无法获取，需要在 chromeOptions 添加 androidProcess 即可
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(8)

    def teardown(self):
        self.driver.quit()

    def main_run(self):
        # 刚打开微信时，页面加载时间未知，
        # 需要通过find_element触发隐式等待，防止后续操作失败
        print(1)
        sleep(25)
        print(2)
        self.driver.implicitly_wait(6)
        print(3)
        self.driver.find_element(AppiumBy.ID, 'index-kw').click()
        sleep(5)
        self.driver.find_element(AppiumBy.ID, 'index-kw').send_keys('黑洞')
        sleep(5)


if __name__ == '__main__':
    demo_ = TestDemo()
    demo_.main_run()
    demo_.teardown()
