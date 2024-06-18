# -*- coding: utf-8 -*-
import cv2, numpy

image = cv2.imread('captcha1.png')
image = cv2.circle(image, (217,125), radius=10, color=(0, 0, 255), thickness=1)
image = cv2.circle(image, (119,195), radius=10, color=(0, 0, 255), thickness=1)
image = cv2.circle(image, (72,208), radius=10, color=(0, 0, 255), thickness=1)
cv2.imwrite('captcha1_label.png', image)
