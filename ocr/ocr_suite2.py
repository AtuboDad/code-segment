# -*- coding: utf-8 -*-
import ddddocr
import cv2 as cv

det = ddddocr.DdddOcr(det=False, ocr=False)

target_img = r'E:\workspaces\pythonspaces\QT_downloader\simulation\ocr\cutPic.png'
bg_img = r'E:\workspaces\pythonspaces\QT_downloader\simulation\ocr\bgPic.jpg'
with open(target_img, 'rb') as f:
    target_bytes = f.read()

with open(bg_img, 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=True)

print(res)

img_target = cv.imread(bg_img)
left_up = (res['target'][0], res['target'][1])
right_down = (res['target'][0] + 108, res['target'][1] + 108)
cv.rectangle(img_target, left_up, right_down, (0, 0, 255), 2)
cv.imshow('res', img_target)
cv.waitKey(0)
cv.destroyAllWindows()