# -*- coding: utf-8 -*-

import cv2
from simulation.chaojiying.chaojiying import ChaoJiYing


USERNAME = '17605922335'
PASSWORD = 'FaXin123456'
SOFT_ID = '935942'
CAPTCHA_KIND = '9004'
FILE_NAME = 'captcha1.png'

client = ChaoJiYing(USERNAME, PASSWORD, SOFT_ID)
result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
print(result)
# {'err_no': 0, 'err_str': 'OK', 'pic_id': '1177711570870090001', 'pic_str': '217,125|119,195|72,208', 'md5': '40560df0b6c55395e9c54e5276a82793'}

pic_str = result['pic_str']

img = cv2.imread(FILE_NAME, 1)
pre_long = 20

pic_point_list = pic_str.split('|')
result_list = []
for pic_point_item in pic_point_list:
    x_y_point = pic_point_item.split(',')
    x, y = int(x_y_point[0]), int(x_y_point[1])
    # result_list.append((x, y))

    cv2.rectangle(img, (x - pre_long, y - pre_long), (x + pre_long, y + pre_long), (0, 0, 255), 2)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

