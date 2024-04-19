import PyPDF2

# 创建一个PDF文档的写入器
output = PyPDF2.PdfWriter()

# 打开第一个PDF文件
with open('E:\\workspaces\\2024\\4月\\停车资料\\1.pdf', 'rb') as file1:
    reader = PyPDF2.PdfReader(file1)
    # 将第一个PDF文件的所有页面添加到输出
    for page in reader.pages:
        output.add_page(page)

# 打开第二个PDF文件
with open('E:\\workspaces\\2024\\4月\\停车资料\\SCAN0001.pdf', 'rb') as file2:
    reader = PyPDF2.PdfReader(file2)
    # 将第二个PDF文件的所有页面添加到输出
    for page in reader.pages:
        output.add_page(page)

# 打开第二个PDF文件
with open('E:\\workspaces\\2024\\4月\\停车资料\\SCAN0002.pdf', 'rb') as file2:
    reader = PyPDF2.PdfReader(file2)
    # 将第二个PDF文件的所有页面添加到输出
    for page in reader.pages:
        output.add_page(page)

# 打开第二个PDF文件
with open('E:\\workspaces\\2024\\4月\\停车资料\\SCAN0000.pdf', 'rb') as file2:
    reader = PyPDF2.PdfReader(file2)
    # 将第二个PDF文件的所有页面添加到输出
    output.add_page(reader.pages[0])

# 保存合并后的PDF文件
with open('merged.pdf', 'wb') as merged_file:
    output.write(merged_file)