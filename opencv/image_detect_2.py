# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def template_demo():
    template1 = cv.imread("./slide.jpg")
    target1 = cv.imread("./target1.jpg")


    template = cv.Canny(template1, 100, 200)
    target = cv.Canny(target1, 100, 200)

    # target = cv.cvtColor(target1, cv.COLOR_GRAY2RGB)
    # template = cv.cvtColor(template1, cv.COLOR_GRAY2RGB)

    tpl = cv.resize(template, (int(template.shape[0] / 5), int(template.shape[1] / 5)))

    # cv.imshow("template image", tpl)
    # cv.imshow("target image", target)

    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # 各种匹配算法
    th, tw = tpl.shape[:2]  # 获取模板图像的高宽
    for md in methods:
        result = cv.matchTemplate(target, tpl, md)
        # result是我们各种算法下匹配后的图像
        # cv.imshow("%s"%md,result)
        # 获取的是每种公式中计算出来的值，每个像素点都对应一个值
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc  # tl是左上角点
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)  # 右下点
        cv.rectangle(target, tl, br, (0, 0, 255), 2)  # 画矩形
        cv.imshow("match-%s" % md, target)


src = cv.imread("./target1.jpg")  # 读取图片
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)  # 创建GUI窗口,形式为自适应
cv.imshow("input image", src)  # 通过名字将图像和窗口联系
template_demo()
cv.waitKey(0)  # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
cv.destroyAllWindows()  # 销毁所有窗口
