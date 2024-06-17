# -*- coding: utf-8 -*-
import ddddocr

ocr = ddddocr.DdddOcr(show_ad=False)
with open('test4.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)
