# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from PIL import Image
import jieba
import numpy
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS


def chinese_jieba(text):
    # 通过jieba工具将中文文本做处理，并返回指定格式的内容
    wordlist_jieba = jieba.cut(text)
    text_jieba = ' '.join(wordlist_jieba)
    return text_jieba


def main(filename):
    with open(filename, 'rb') as f:
        text = chinese_jieba(f.read().decode())

    mask_pic = numpy.array(Image.open('test.jpg'))  # 打开图像处理，设置遮罩层

    # 设置固定的词个数为0
    # stopwords = {'黑娃':0,'白嘉轩':0}
    # 也可以按照下面格式设置
    stopwords = set(STOPWORDS)
    stopwords = stopwords.union(set(['黑娃', '白嘉轩']))  # 将不想在词云上出现的词，放入集合中，也就是设置固定词个数为0

    wordclod = WordCloud(
        background_color='white',  # 设置背景颜色，默认是黑色
        margin=0,
        max_words=2000,  # 关键字的个数
        max_font_size=100,  # 字体大小
        font_path=r'D:\workspaces\pythonspaces\images_transform\fonts_dir\SimHei.ttf',  # 设置中文识别
        mask=mask_pic,  # 添加遮罩层,也就是设置词云形状
        stopwords=stopwords,  # 过滤固定的词
    ).generate(text)  # 将text里面所有的词统计,产生词云

    # image_colors = ImageColorGenerator(mask_pic)

    plt.imshow(wordclod)
    # plt.imshow(wordclod.recolor(color_func=image_colors))
    plt.axis('off')
    plt.show()
    wordclod.to_file('cloud.jpg')  # 保存图片


if __name__ == "__main__":
    filename = 'cloud.txt'
    main(filename)

