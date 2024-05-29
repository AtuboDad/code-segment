# -*- coding: utf-8 -*-
import time
import uiautomator2 as u2
# from chromedriver1 import ChromeDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from atx.ext.chromedriver import ChromeDriver
from selenium.webdriver.chrome.service import Service


# python -m pip
d = u2.connect('c53f0c08')
# d.app_start('com.tencent.mm')
d.app_start('com.github.android_app_bootstrap')

app = d.app_current()

# 查看包名: adb shell dumpsys window w |findstr \/ |findstr name=
options = webdriver.ChromeOptions()

# options.add_experimental_option('w3c', False)
options.add_experimental_option('androidDeviceSerial', d.serial)
options.add_experimental_option('androidPackage', app.get('package'))
options.add_experimental_option('androidUseRunningApp', True)

# options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
# options.add_experimental_option('appActivity', '.ui.LauncherUI')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
print(driver.current_url)
driver.implicitly_wait(3)

time.sleep(3)
d(text='Login').click()
time.sleep(3)
d(text='Baidu').click()

kw_input = driver.find_element(By.ID, 'index-kw')
driver.execute_script('arguments[0].click()', kw_input)
driver.implicitly_wait(3)
driver.find_element(By.ID, 'index-kw').send_keys('Python')
driver.implicitly_wait(3)
click_button = driver.find_element(By.ID, 'index-bn')
driver.execute_script('arguments[0].click()', click_button)
driver.implicitly_wait(3)
driver.quit()