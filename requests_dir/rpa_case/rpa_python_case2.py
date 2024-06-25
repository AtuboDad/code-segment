# -*- coding: utf-8 -*-
import os

import rpa as r

r.tagui_location('D:/softs')
r.init(visual_automation=True, chrome_browser = False)

print(r.read(r'hello.png'))
r.hover(r'hello.png')
print(r.read(r.mouse_x(), r.mouse_y(), r.mouse_x() + 400, r.mouse_y() + 200))
r.close()
