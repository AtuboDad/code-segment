# -*- coding: utf-8 -*-
import cv2
import numpy as np


# 对滑块进行二值化处理
def handle_img1(image):
    kernel_2 = np.ones((8, 8), np.uint8)  # 去滑块的前景噪声内核
    gray_2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width_2, height_2 = gray_2.shape
    for h in range(height_2):
        for w in range(width_2):
            if gray_2[w, h] == 0:
                gray_2[w, h] = 96
    # cv2.imshow('gray', gray)
    binary = cv2.inRange(gray_2, 96, 96)
    res = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_2)  # 开运算去除白色噪点
    # cv2.imshow('res', res)
    return res

img_target = cv2.imread('./test1.png')
img_template = cv2.imread('./test2.png')

img_target = cv2.resize(img_target, (340, 212))
img_template = cv2.resize(img_template, (67, 67))

tpl = handle_img1(img_template)

blurred = cv2.GaussianBlur(img_target, (3, 3), 0)  # 目标图高斯滤波
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, target = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)  # 目标图二值化

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,5))
dst = cv2.dilate(target, kernel, iterations=1)

cv2.imshow("template", tpl)
cv2.imshow("target", target)
cv2.imshow("dst", dst)

method = cv2.TM_CCOEFF_NORMED
width, height = tpl.shape[:2]
result = cv2.matchTemplate(dst, tpl, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
left_up = max_loc
right_down = (left_up[0] + height, left_up[1] + width)
cv2.rectangle(img_target, left_up, right_down, (0, 0, 255), 2)
cv2.imshow('res', img_target)

cv2.waitKey(0)
cv2.destroyAllWindows()
