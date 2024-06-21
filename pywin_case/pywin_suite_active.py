# -*- coding: utf-8 -*-
import time
import win32con
import win32gui
import pyautogui


def main():
    # chatroom = 'RdCard_Demo_C - Visual Studio Code [Administrator]'
    # win = win32gui.FindWindow('Chrome_WidgetWin_1', chatroom)

    chatroom = '微信'
    # win = win32gui.FindWindow('CefWebViewWnd', chatroom)
    win = win32gui.FindWindow('WeChatMainWndForPC', chatroom)
    # win32gui.SendMessage(win, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)

    print("找到窗口句柄：%x" % win)
    rect = win32gui.GetWindowRect(win)
    x = rect[0]
    y = rect[1]
    print(x, y)

    if win != 0:
        # 这种方式，可以激活在菜单栏的微信程序，而不会去找右下角的最小化 ICON
        win32gui.ShowWindow(win, win32con.SW_SHOWMAXIMIZED)
        win32gui.SetActiveWindow(win)
        # win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        time.sleep(2)
        # win32gui.CloseWindow(win)
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        time.sleep(2)


        # # win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 0, 0, 300, 500, win32con.SWP_SHOWWINDOW)
        # win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 0, 0, 300, 500,
        #                       win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
        # win32gui.SetForegroundWindow(win)  # 获取控制
        # win32gui.SetWindowPos(win, win32con.HWND_NOTOPMOST, int(x), int(y), 0, 0, win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        # time.sleep(1)
        hwclass = win32gui.GetClassName(win)
        tit = win32gui.GetWindowText(win)
        print('已启动【' + str(hwclass) + '】窗口')
        print('已启动【' + str(tit) + '】窗口')
    else:
        print('找不到【%s】窗口' % chatroom)
        exit()


if __name__ == '__main__':
    main()
