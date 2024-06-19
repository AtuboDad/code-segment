# -*- coding: utf-8 -*-
import time
import office

# 一行代码，实现转换
start_time = time.time()
office.pdf.pdf2imgs(
    pdf_path='./20221108115033042466373.pdf',
    out_dir='./results'
)

end_time = time.time()
print(end_time - start_time)
