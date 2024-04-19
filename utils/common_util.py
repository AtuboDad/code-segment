# -*- coding: utf-8 -*-
import json
import time
import fitz
import requests
import PIL.ExifTags
from PIL import Image


def read_file(file_name, chunk_size=512):
    """
    # 用于形成二进制数据
    :param file_name:
    :param chunk_size:
    :return:
    """
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def return_data(data):
    return json.dumps(data, ensure_ascii=False)


def parse_image_from_path(images_string):
    images_string = str(images_string)
    images_string_items = json.loads(images_string)

    images_string_array = []
    for images_string_item in images_string_items:
        if images_string_item is not None:
            images_string_array.append(images_string_item)
    return images_string_array


def find_parent_path(file_absolute_path, char_1):
    count = 0
    index_arr = []

    for each_char in file_absolute_path:
        count += 1
        if each_char == char_1:
            index_arr.append(count - 1)

    if len(index_arr) > 0:
        return file_absolute_path[0:index_arr[len(index_arr) - 1]]
    return ''


def find_file_name(file_absolute_path, char_1):
    count = 0
    index_arr = []

    for each_char in file_absolute_path:
        count += 1
        if each_char == char_1:
            index_arr.append(count - 1)

    if len(index_arr) > 0:
        return file_absolute_path[index_arr[len(index_arr) - 1] + 1:]
    return file_absolute_path


def pdf2pic(pdf, temp_dir):
    try:
        doc = fitz.open(pdf)
    except Exception as e:
        return None
    pdf_image_list = []
    file_name_extend = str(pdf).split('/')[-1:][0]
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        if len(file_name_extend) > 100:
            file_name_extend = str(file_name_extend[:100])
        pm.writePNG('%s%s.jpg' % (temp_dir + file_name_extend, str(pg + 1)))
        pdf_image_list.append('%s%s.jpg' % (temp_dir + file_name_extend, str(pg + 1)))
    return pdf_image_list


def can_read(pdf):
    try:
        doc = fitz.open(pdf)
        doc.close()
        return True
    except Exception as e:
        return False


def notify_back(notify_url, data):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8;'
    }
    params = json.dumps(data)
    response = requests.post(notify_url, data=params, headers=headers)
    return response.text


def is_phone_image(image):
    w, h = image.size
    if w > 1920:
        return True
    if hasattr(image, '_getexif'):  # only present in JPEGs
        for orientation in PIL.ExifTags.TAGS.keys():
            if PIL.ExifTags.TAGS[orientation] == 'Orientation':
                break
        e = image._getexif()  # returns None if no EXIF data
        if e is not None:
            return True
    return False
