# -*- coding: utf-8 -*-
import ddddocr
import cv2

det = ddddocr.DdddOcr(det=True)

with open("test3.png", 'rb') as f:
    image = f.read()

poses = det.detection(image)
print(poses)

im = cv2.imread("test3.png")

count = 0
for box in poses:
    x1, y1, x2, y2 = box
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    if count > 6:
        break
    count = count + 1

cv2.imwrite("result.png", im)
