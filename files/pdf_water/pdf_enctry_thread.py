# -*- coding: utf-8 -*-
import pikepdf

inFile = "重塑心灵电子书.pdf"  # pdf文件路径
outFile = "重塑心灵电子书_解密.pdf"  # pdf文件路径

count = 0
jiemiInfo = ''
try:
    filePath = inFile
    tips = "正在转换第" + str(count + 1) + "个文件"
    with pikepdf.open(filePath, allow_overwriting_input=True) as pdf:
        num_pages = len(pdf.pages)
        pdf.save(outFile)
    count += 1
except Exception as e:
    pass
