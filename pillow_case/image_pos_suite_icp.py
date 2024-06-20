# -*- coding: utf-8 -*-
import io

import cv2 as cv
import numpy as np
from PIL import Image, ImageChops


# 模板匹配(用于寻找缺口有点误差)
def template_match(file_name, img_target: bytes = None, background_bytes: bytes = None):
    target = cv.imdecode(np.frombuffer(img_target, np.uint8), cv.IMREAD_ANYCOLOR)

    background = cv.imdecode(np.frombuffer(background_bytes, np.uint8), cv.IMREAD_ANYCOLOR)

    target_2 = cv.resize(target, (500, 190))
    background_2 = cv.resize(background, (66, 66))

    background = cv.Canny(background_2, 100, 200)
    target = cv.Canny(target_2, 100, 200)

    background = cv.cvtColor(background, cv.COLOR_GRAY2RGB)
    target = cv.cvtColor(target, cv.COLOR_GRAY2RGB)

    res = cv.matchTemplate(background, target, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    left_up = (int(max_loc[0]), int(max_loc[1]))
    right_down = (int(max_loc[0]) + 66, int(max_loc[1]) + 66)

    cv.rectangle(target_2, left_up, right_down, (0, 0, 255), 2)
    cv.imshow('res', target_2)
    print(left_up, right_down)


if __name__ == '__main__':
    target_img = './verify_image.png'
    template_img = './verify_image_slide.png'

    with open(target_img, 'rb') as f:
        target_bytes = f.read()

    with open(template_img, 'rb') as f:
        background_ = f.read()

    template_match(target_img, target_bytes, background_)
    cv.waitKey(0)
    cv.destroyAllWindows()
