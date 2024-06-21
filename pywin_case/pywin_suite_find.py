# -*- coding: utf-8 -*-
import time
import win32con
import win32gui
import pyautogui


def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


def show_window_attr(hWnd):
    '''
    显示窗口的属性
    :return:
    '''
    if not hWnd:
        return

    # 中文系统默认title是gb2312的编码
    title = win32gui.GetWindowText(hWnd)
    clsname = win32gui.GetClassName(hWnd)

    print('窗口句柄:%s | %s | %s ' % (hWnd, title, clsname))


def show_windows(hWndList):
    for h in hWndList:
        show_window_attr(h)


def main():
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    show_windows(hWndList)


if __name__ == '__main__':
    main()
