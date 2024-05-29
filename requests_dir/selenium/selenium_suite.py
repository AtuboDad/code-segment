# -*- coding: utf-8 -*-
import time
from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions # 用来模拟手机端操作


WIDTH = 600
HEIGHT = 800
PIXEL_RATIO = 3.0
# UA 必须要是手机设备的
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://m.baidu.com')
time.sleep(1)
inputs = driver.find_element('index-kw')
# TouchActions(driver).tap(inputs).perform() # 模拟触控
driver.close()
driver.quit()