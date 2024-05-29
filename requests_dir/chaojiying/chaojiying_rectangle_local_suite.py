# -*- coding: utf-8 -*-
import cv2
from simulation.chaojiying.chaojiying import ChaoJiYing


FILE_NAME = 'captcha1.png'

json_str = {'err_no': 0, 'err_str': 'OK', 'pic_id': '1221210580899550036', 'pic_str': '64,78|250,115|49,165|155,225', 'md5': 'f838268b61f1b77deebaacd3878ebc95'}
pic_str = json_str['pic_str']

img = cv2.imread(FILE_NAME, 1)
pre_long = 20

pic_point_list = pic_str.split('|')
result_list = []
for pic_point_item in pic_point_list:
    x_y_point = pic_point_item.split(',')
    x, y = int(x_y_point[0]), int(x_y_point[1])

    cv2.rectangle(img, (x - pre_long, y - pre_long), (x + pre_long, y + pre_long), (0, 0, 255), 2)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
