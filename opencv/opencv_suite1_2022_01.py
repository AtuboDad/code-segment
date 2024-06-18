# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

maxvalue = 255

img = cv.imread('./1.jpg')

# w, h, _ = img.shape
# 576 1024
# cv.line(img, (0, 0), (1024, 576), 1)
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv.polylines(img, [pts], True, (0, 255, 255))

# img.itemset((10, 10, 2), 100)
# cv.imshow('name', img)
# img1 = cv.imread('./1.jpg', 0)
# cv.imshow('name1', img1)
value = 100

# gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
gauss = cv.GaussianBlur(img, (3, 3), 1)

a, binary = cv.threshold(gauss, value, maxvalue, cv.THRESH_BINARY)
b, binary_inv = cv.threshold(gauss, value, maxvalue, cv.THRESH_BINARY_INV)
c, trunc = cv.threshold(gauss, value, maxvalue, cv.THRESH_TRUNC)
d, to_zero = cv.threshold(gauss, value, maxvalue, cv.THRESH_TOZERO)
e, to_zero_inv = cv.threshold(gauss, value, maxvalue, cv.THRESH_TOZERO_INV)
if (a):
    cv.imshow("Binary", binary)
if (b):
    cv.imshow("Binary_INV", binary_inv)
if (c):
    cv.imshow("TRUNC", trunc)
if (d):
    cv.imshow("TO_ZERO", to_zero)
if (e):
    cv.imshow("TO_ZERO_INV", to_zero_inv)

# cv.imshow('frame', img)

cv.waitKey(0)
cv.destroyAllWindows()
