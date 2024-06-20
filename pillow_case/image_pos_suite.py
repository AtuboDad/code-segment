# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def get_pos(image):
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    canny = cv.Canny(blurred, 200, 400)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.imshow('image', image)
            return x
    return 0


# 对滑块进行二值化处理
def handle_img1(image):
    kernel = np.ones((8, 8), np.uint8)  # 去滑块的前景噪声内核
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    width, heigth = gray.shape
    for h in range(heigth):
        for w in range(width):
            if gray[w, h] == 0:
                gray[w, h] = 96
    # cv.imshow('gray', gray)
    binary = cv.inRange(gray, 96, 96)
    res = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开运算去除白色噪点
    # cv.imshow('res', res)
    return res


# 模板匹配(用于寻找缺口有点误差)
def template_match(img_target, img_template):

    img_target = cv.resize(img_target, (340, 212))
    img_template = cv.resize(img_template, (67, 67))

    tpl = handle_img1(img_template)  # 误差来源就在于滑块的背景图为白色
    blurred = cv.GaussianBlur(img_target, (3, 3), 0)  # 目标图高斯滤波
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, target = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)  # 目标图二值化
    cv.imshow("template", tpl)
    cv.imshow("target", target)
    method = cv.TM_CCOEFF_NORMED
    width, height = tpl.shape[:2]
    result = cv.matchTemplate(target, tpl, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    left_up = max_loc
    right_down = (left_up[0] + height, left_up[1] + width)
    cv.rectangle(img_target, left_up, right_down, (0, 0, 255), 2)
    cv.imshow('res', img_target)
    print(left_up, right_down)


def cut_img(img):
    img = cv.imread(img)
    w, h, g = img.shape
    print(w, h)
    width = 0
    dst = img[width:w - width, width:h - width]  # 裁剪坐标为[y0:y1, x0:x1]
    cv.imwrite("result.png", dst)


if __name__ == '__main__':
    img0 = cv.imread('./test1.png')
    cut_img('./test2.png')
    img1 = cv.imread('./result.png')
    template_match(img0, img1)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #