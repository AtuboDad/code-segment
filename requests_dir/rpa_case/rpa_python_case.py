# -*- coding: utf-8 -*-
import os

import rpa as r

r.tagui_location('D:/softs')
r.init(visual_automation=True)

r.url('http://www.baidu.com')
r.wait(20000)
r.type('#kw', '美女')
r.wait(2)
r.click('#su')
r.wait(2)
r.click('.c-container > div > div > div > a')
r.wait(5)
r.type(600, 300, 'open source')
r.click(900, 300)
r.mouse('down')
r.hover(r.mouse_x() + 300, r.mouse_y())
r.mouse('up')
r.close()
