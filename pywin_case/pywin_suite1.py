# -*- coding: utf-8 -*-
import win32con
import win32gui
import pyautogui

hwnd_title = {}
def callback(hwnd, extra):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        # w = rect[2] - x
        # h = rect[3] - y
        # print("Window %s:" % win32gui.GetWindowText(hwnd))
        # print("\tLocation: (%d, %d)" % (x, y))
        # print("\t    Size: (%d, %d)" % (w, h))
        hwclass = win32gui.GetClassName(hwnd)
        hwnd_title.update({hwnd: {'title': win32gui.GetWindowText(hwnd), 'className': str(hwclass), 'x': x, 'y': y}})

        if 'Code' == str(win32gui.GetWindowText(hwnd)):
            print('Code', x, y)
            # 置顶
            # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
            # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
            #                       win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
            # 取消置顶
            # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, int(x), int(y), 0, 0, win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)


def main():
    win32gui.EnumWindows(callback, None)
    for h, t in hwnd_title.items():
        if t :
            print(h, '|', t['title'], '|', t['className'], '|', t['x'], '|', t['y'])
            # if '微信' == t['title']:
            #     pyautogui.moveTo(int(t['x']), int(t['y']), duration=0.25)
    # hwnd = win32gui.FindWindow(None, "微信")
    # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    # # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
    # #                       win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
    # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

if __name__ == '__main__':
    main()
