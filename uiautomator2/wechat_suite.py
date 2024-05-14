# -*- coding: utf-8 -*-
import time
import uiautomator2 as u2
from chromedriver2 import ChromeDriver   #将chromedriver.py和该脚本放在同一目录下
from selenium.webdriver.common.by import By

d = u2.connect('c53f0c08')
d.app_start('com.tencent.mm')
time.sleep(1)
driver = ChromeDriver(d).driver()
time.sleep(3)


context = 'WEBVIEW_com.tencent.mm:tools'
driver.switch_to(context)

time.sleep(3)
kw_input = driver.find_element('id', 'index-kw')
driver.execute_script('arguments[0].click()', kw_input)
driver.implicitly_wait(3)
driver.find_element('id', 'index-kw').send_keys('Python')
driver.implicitly_wait(3)
click_button = driver.find_element('id', 'index-bn')
driver.execute_script('arguments[0].click()', click_button)
driver.implicitly_wait(3)
driver.quit()
