# -*- coding: utf-8 -*-
import os
import win32file

# popen返回文件对象，同open操作一样
# f = os.popen(r"dir /a D:\workspaces\pythonspaces\QT_downloader\simulation\cmd\cmd_suite.py")
#
# l = f.read()
# print(l)
# f.close()


result = win32file.GetFileAttributesEx(r"D:\test.docx")
print(result)
