# -*- coding: utf-8 -*-

import os


def list_files_in_directory(directory, level=1):
    """
    列出指定目录下的所有文件（包括子目录中的文件），但不超过指定层级。
    """
    for root, dirs, files in os.walk(directory):
        # 当前目录层级
        current_level = root.count(os.sep)
        # 如果当前层级大于等于设定的级数，则不再遍历子目录
        if current_level >= level:
            for dir_ in dirs:
                yield os.path.join(root, dir_)
            dirs.clear()  # 清空目录列表，避免遍历更深的目录
        for file in files:
            yield os.path.join(root, file)


# 使用示例
directory = 'E:\\workspaces\\2024'  # 替换为你的目录路径
level = 3  # 设置目录层级

with open('E:\\workspaces\\文件列表.txt', 'w', encoding='utf-8') as f:
    f.write('2024\r')
    for file_path in list_files_in_directory(directory, level):
        f.write('\t' + str(file_path)[19:] + '\r')

    f.close()

directory = 'E:\\workspaces\\2024技术相关'  # 替换为你的目录路径
level = 3  # 设置目录层级

with open('E:\\workspaces\\文件列表技术相关.txt', 'w', encoding='utf-8') as f:
    f.write('2024技术相关\r')
    for file_path in list_files_in_directory(directory, level):
        f.write('\t' + str(file_path)[23:] + '\r')

    f.close()