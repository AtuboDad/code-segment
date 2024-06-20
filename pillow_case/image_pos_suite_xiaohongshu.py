# -*- coding: utf-8 -*-
import io

import cv2 as cv
import numpy as np
from PIL import Image, ImageChops


def clear_image(image_path) -> np.ndarray:
    img = cv.imread(image_path)
    rows, cols, channel = img.shape
    min_x = 255
    min_y = 255
    max_x = 0
    max_y = 0

    for x in range(1, rows):
        for y in range(1, cols):
            t = set(img[x, y])
            if len(t) >= 2:
                if x <= min_x:
                    min_x = x
                elif x >= max_x:
                    max_x = x
                if y <= min_y:
                    min_y = y
                elif y > max_y:
                    max_y = y

    img1 = img[min_x:max_x, min_y:max_y]
    return img1


# 模板匹配(用于寻找缺口有点误差)
def template_match(file_name, img_target: bytes = None, background_bytes: bytes = None):

    target = cv.imdecode(np.frombuffer(img_target, np.uint8), cv.IMREAD_ANYCOLOR)

    background = cv.imdecode(np.frombuffer(background_bytes, np.uint8), cv.IMREAD_ANYCOLOR)

    target_2 = cv.resize(target, (400, 200))
    background_2 = cv.resize(background, (60, 60))
    print(type(target_2))

    background = cv.Canny(background_2, 100, 200)
    target = cv.Canny(target_2, 100, 200)

    background = cv.cvtColor(background, cv.COLOR_GRAY2RGB)
    target = cv.cvtColor(target, cv.COLOR_GRAY2RGB)

    print(type(target))
    cv.imshow('background', background)
    cv.imshow('target', target)

    res = cv.matchTemplate(background, target, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    left_up = (int(max_loc[0]), int(max_loc[1]))
    right_down = (int(max_loc[0]) + 56, int(max_loc[1]) + 56)

    cv.rectangle(target_2, left_up, right_down, (0, 0, 255), 2)
    cv.imshow('res', target_2)
    print(left_up, right_down)


if __name__ == '__main__':
    # target_img = './bgPic.jpg'
    # template_img = './cutPic.png'
    target_img = './verify_image.png'
    template_img = './verify_image_slide.png'
    template_img_clear = './verify_image_slide_clear.png'

    img1 = clear_image(template_img)
    cv.imwrite(template_img_clear, img1)

    with open(target_img, 'rb') as f:
        target_bytes = f.read()

    with open(template_img_clear, 'rb') as f:
        background_ = f.read()

    template_match(target_img, target_bytes, background_)
    cv.waitKey(0)
    cv.destroyAllWindows()
