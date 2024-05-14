# -*- coding: utf-8 -*-
import time
import uiautomator2 as u2
from chromedriver1 import ChromeDriver   #将chromedriver.py和该脚本放在同一目录下

d = u2.connect('c53f0c08')
d.app_start('com.github.android_app_bootstrap')
time.sleep(3)
d(text='Login').click()
time.sleep(3)
d(text='Baidu').click()
driver = ChromeDriver(d).driver()
time.sleep(3)
# 172.16.20.239

kw_input = driver.find_element('id', 'index-kw')
driver.execute_script('arguments[0].click()', kw_input)
driver.implicitly_wait(3)
driver.find_element('id', 'index-kw').send_keys('Python')
driver.implicitly_wait(3)
click_button = driver.find_element('id', 'index-bn')
driver.execute_script('arguments[0].click()', click_button)
driver.implicitly_wait(3)
driver.quit()
