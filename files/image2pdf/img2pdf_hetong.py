# -*- coding: utf-8 -*-

import os
import uuid

import PIL.ExifTags
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from imghdr import what

from utils import common_util

pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))


real_page_size = A4

def split_image(src, dst_path, uuid_fir_name, images_list):
    img = PIL.Image.open(src)
    w, h = img.size
    document_width, document_height = A4
    floatW = float(w)
    floatH = float(h)
    img_height = 2500
    float_value = floatH / img_height
    row_num = int(floatH / img_height)

    if float_value > row_num:
        row_num = row_num + 1
    col_num = 1

    print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
    print('开始处理图片切割, 请稍候...')

    s = os.path.split(src)
    if dst_path == '':
        dst_path = s[0]
    fn = s[1].split('.')
    basename = fn[0]
    ext = fn[-1]

    num = 0
    rowheight = h // row_num
    col_width = w // col_num
    image_item_files = []

    is_phone = False
    if hasattr(img, '_getexif'):  # only present in JPEGs
        e = img._getexif()  # returns None if no EXIF data
        if e is not None:
            print('手机图片')
            is_phone = True

    if not os.path.exists(dst_path + uuid_fir_name):
        print('切割图片时文件所在父目录不存在, 创建')
        os.makedirs(dst_path + uuid_fir_name)

    if h > 2 * w and not is_phone:
        for r in range(row_num):
            box_height = (r + 1) * img_height
            for c in range(col_num):
                if (r + 1) == row_num:
                    box_height = h
                box = (c * col_width, r * img_height, (c + 1) * col_width, box_height)
                print(dst_path + uuid_fir_name + '/' + basename + '_' + str(num) + '.' + ext)
                image_item_files.append(dst_path + uuid_fir_name + '/' + basename + '_' + str(num) + '.' + ext)
                img.crop(box).save(os.path.join(dst_path,  uuid_fir_name + '/' + basename + '_' + str(num) + '.' + ext), 'jpeg')
                num = num + 1
        images_list.append(image_item_files)
        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        image_item_files.append(src)
        images_list.append(image_item_files)


def rotate_img_to_proper(image):
    global orientation
    w, h = image.size
    a4_width, a4_height = real_page_size
    try:
        max_value = max(w, h)
        rate = a4_height / max_value
        return image.resize((int(w * rate), int(h * rate)), Image.ANTIALIAS)
    except:
        pass

    return image


def generate_pdf(output_file_name='Output.pdf', images_list=None, images=None):

    parent_path = common_util.find_parent_path(output_file_name, '/')
    if parent_path != '' and parent_path != '/' and not os.path.exists(parent_path):
        print('parent dir not exist, creating')
        os.makedirs(parent_path)
    img_doc = canvas.Canvas(output_file_name)  # pagesize=letter
    img_doc.setTitle('image2pdf.PDF')
    img_doc.setAuthor('atubo')
    img_doc.setPageSize(A4)
    document_width, document_height = A4
    start_index = 0
    file_index = 1

    for image_file_items in images_list:

        total_file_index = len(image_file_items)
        file_name = images[start_index]
        file_name_extend = str(file_name).split('/')[-1:][0]
        start_index = start_index + 1
        for image in image_file_items:
            try:
                image_file = PIL.Image.open(image)
                image_file = rotate_img_to_proper(image_file)

                image_width, image_height = image_file.size

                if not (image_width > 0 and image_height > 0):
                    raise Exception
                image_aspect = image_height / float(image_width)
                image_aspect_h = image_width / float(image_height)

                print_width = document_width - 20
                print_height = document_width * image_aspect - 5
                # print document_height - (document_width * image_aspect - 5)
                if 50 < document_height - (document_width * image_aspect - 5) < 60:
                    print_height = document_width * image_aspect - 35
                # if wRate < hRate:
                if image_aspect_h < image_aspect and document_height * image_aspect_h < document_width:
                    print_width = document_height * image_aspect_h
                    print_height = document_height - 80

                img_doc.setFont('SimHei', 16)
                # img_doc.drawString(30, 820, "电子公证书纸质附件粘附页")
                img_doc.setFont('SimHei', 12)

                # 填充黑块
                # img_doc.rect(0, 2 * inch, 0.2 * inch, 0.3 * inch, fill=1)
                # 填充颜色
                # img_doc.setFillColor(green)
                # sub_text = "内容:公证书附件--" + file_name_extend
                # img_doc.drawString(30, 800, sub_text)
                # subTextLength = img_doc.stringWidth(sub_text)
                # subTextPrefixLength = img_doc.stringWidth('内容:')
                img_doc.setLineWidth(0.5)
                # img_doc.line(30 + subTextPrefixLength, 798, 30 + subTextLength, 798)
                # img_doc.drawPath(sub_text)
                img_doc.setFont('SimHei', 12)
                # img_doc.drawString(document_width - 90, 820, "共{}页".format(len(images_list)))
                img_doc.drawImage(ImageReader(image_file), 10,
                                 document_height - print_height - 20, width=print_width,
                                 height=print_height, preserveAspectRatio=True)
                img_doc.drawString(document_width / 2, 10, "{}/{}".format(file_index, len(images_list)))
                image_file.close()
                # img_doc.drawString(10, 30, '【测试测试的撒旦萨大赛的撒旦撒旦萨大赛的撒旦萨大赛的测试的撒旦撒旦萨达的撒旦萨】')
                img_doc.showPage()
            except Exception as e:
                print('error:', e, image)
        file_index = file_index + 1
    img_doc.save()
    for image_file_items in images_list:
        for image_file_item in image_file_items:
            if os.path.exists(image_file_item) and image_file_item.startswith('./images'):
                try:
                    os.remove(image_file_item)
                except Exception as e:
                    print('error:', e)


def img_search(src_path, images):
    for lists in os.listdir(src_path):
        path = os.path.join(src_path, lists)
        if os.path.isfile(path):
            a = path.split('.')
            if a[-1] in ['jpg', 'png', 'JPEG']:
                images.append(path)


def execute():
    images = [
        '../resources/images/sx1.png'
    ]
    # img_search('.\\test_images', images)
    dst_path = '../output/'
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    images_list = []
    uuid_fir_name = uuid.uuid4()

    if (dst_path == '') or os.path.exists(dst_path):

        temp_dir_list = []

        for image_src in images:
            is_image = what(image_src)
            if is_image is None:
                return {'error': 'This image is not a picture, check please.'}
            split_image(image_src, dst_path, str(uuid_fir_name), images_list)
            temp_dir_list.append(dst_path + str(uuid_fir_name))
        print(images_list)
        generate_pdf('../output/Output.pdf', images_list, images)
        delete_temp(temp_dir_list)
        return {'success': 'success'}
    else:
        print('图片输出目录 %s 不存在！' % dst_path)


def delete_temp(temp_dirs):
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            print('Delete temp dir: ' + str(temp_dir) + '.')
            os.rmdir(temp_dir)


if __name__ == '__main__':
    result = execute()
    print(result)
