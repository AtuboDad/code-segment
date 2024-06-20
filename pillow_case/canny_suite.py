# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


target_img = r'D:\workspaces\pythonspaces\QT_downloader\simulation\pillow_case\test5.png'
with open(target_img, 'rb') as f:
    target_bytes = f.read()

original_img = cv.imdecode(np.frombuffer(target_bytes, np.uint8), cv.IMREAD_ANYCOLOR)
# original_img = cv.imread("./test5.png")
# cv2_imshow(original_img)

print("\n \n Edge detection in the Original images\n \n ")
# We will find the edges in the image as below
Edge_Org = cv.Canny(original_img, 100, 200)
Edge_Org2 = cv.Canny(original_img, 500, 1000)
cv.imshow('img0', original_img)
cv.imshow('img1', Edge_Org)
cv.imshow('img2', Edge_Org2)

cv.waitKey(0)
cv.destroyAllWindows()
