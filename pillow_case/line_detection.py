# -*- coding: utf-8 -*-
# 道路斑马线检测
import math
import cv2 as cv
import numpy as np

# 定义两个核  （kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
kernel_Ero = np.ones((3, 1), np.uint8)
kernel_Dia = np.ones((3, 5), np.uint8)

# img = cv.imread("./1111.png")
img = cv.imread("./2222.png")
copy_img = img.copy()


# 直线检测
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # apertureSize是sobel算子大小，只能为1,3,5，7
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)  # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv.imshow("image line", image)

# 曲线检测
def curve_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # cv.imshow("image line", gray)
    w, h = gray.shape
    print(w, h)

    point_size = 1
    point_color = (0, 0, 255)  # BGR
    thickness = 4  # 可以为 0 、4、8

    for i in range(w):
        for j in range(h):
            sum_ = sum(image[i][j])
            if sum_ < 765:
                # cv.circle(img, point, point_size, point_color, thickness)
                image[i][j] = [0, 0, 0]
    cv.imshow("image line", image)
cv.imshow("img", copy_img)

# line_detection(copy_img)
curve_detection(copy_img)

cv.waitKey(0)
cv.destroyAllWindows()
