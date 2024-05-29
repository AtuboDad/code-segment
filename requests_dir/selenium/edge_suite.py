# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# 加载msedgedriver驱动
driver = webdriver.Edge(executable_path='msedgedriver.exe')
# 通过get方法发送网址
driver.get("https://www.baidu.com/")
# 设置停顿在页面的秒数
time.sleep(1)
# 查找id名为kw的页面元素，模拟键盘输入值测试
driver.find_element('id', 'kw').send_keys("测试")
# 查找id名为su的页面元素，模拟鼠标进行点击
driver.find_element('id', 'su').click()
# 设置停顿在页面的秒数
time.sleep(1)
# 查找id名为kw的页面元素，进行清空搜索栏
driver.find_element('id', 'kw').clear()
# 设置停顿在页面的秒数
time.sleep(2)
# 退出测试并关闭浏览器
driver.quit()