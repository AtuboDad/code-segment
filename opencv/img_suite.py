# -*- coding: utf-8 -*-
import cv2, numpy

for i in range(0, 1):
    img = cv2.imread('./images/' + str(i) + '.png', 1)
    cv2.imshow('img', img)
    height = img.shape[0]
    width = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 首先我们需要用opencv将图片读取,生成图片的灰度图并反色。
    dst = 255 - gray

    dst_gauss = cv2.GaussianBlur(dst, (19, 19), 0)
    inverted_blurred_image = 255-dst_gauss

    # 利用opencv的高斯模糊对灰度图进行模糊化
    a = cv2.divide(gray, inverted_blurred_image, scale=255)
    # cv2.imshow('a', a)
    cv2.imwrite('./results/' + str(i) + '.jpg', a)
    # 使用opencv的divide方法将灰度图和模糊图融合，并且将所形成的素描风图片保存下来。

