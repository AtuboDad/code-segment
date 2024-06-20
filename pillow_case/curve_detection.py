# -*- coding: utf-8 -*-
import math
import cv2 as cv
import numpy as np

# img = cv.imread("./1111.png")
img = cv.imread("./2222.png")
copy_img = img.copy()

# 曲线检测
def curve_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # apertureSize是sobel算子大小，只能为1,3,5，7
    cv.imshow("edges", edges)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 60, 100, 20)  # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线

    for line in lines:
        # print(line)
        item = line[0]
    #     rho, theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a * rho
    #     y0 = b * rho
    #     x1 = int(x0 + 1000 * (-b))
    #     y1 = int(y0 + 1000 * (a))
    #     x2 = int(x0 - 1000 * (-b))
    #     y2 = int(y0 - 1000 * (a))
    #     cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv.line(image, (item[0], item[1]), (item[2], item[3]), (0, 0, 255), 2)

    cv.imshow("image line", image)

cv.imshow("img", copy_img)
curve_detection(copy_img)
cv.waitKey(0)
cv.destroyAllWindows()