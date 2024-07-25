from PyPDF2 import PdfWriter
 
pdfWriter = PdfWriter()
 
# 按顺序输入对应的页面编号
pdfWriter.append('example.pdf', pages=[1,0])
 
pdfWriter.write('output.pdf')
pdfWriter.close()

