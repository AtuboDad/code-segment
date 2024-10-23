# -*- coding: utf-8 -*-
import pandas as pd
import os
import psycopg2
from datetime import datetime
import numpy as np



dirs = os.listdir("E:\\workspaces\\2024\\10月\\需导入数据")
host = "192.168.131.128"
user = "postgres"
password = "postgres"
dbname = "postgres"
port = "5432"

tablename = "edu_school"


def connect():
    conn = psycopg2.connect(
        host=host, user=user, password=password, dbname=dbname, port=port
    )
    return conn

def test_show_value(df):
    for index, row in df.iterrows():
        print(row[224], row[240], row[241], row[242], row[243], row[244], row[245])

def extract_data(df, tablename, index1=0, index2=45, index3=224, index4=246, type=''):

    conn = connect()

    cursor = conn.cursor()

    # 创建一个列表来存储要插入的数据
    data_to_insert = []
    cursor.execute(
        "SELECT column_name FROM information_schema.columns WHERE table_name = %s AND column_name <> 'id' ORDER BY ordinal_position",
        (tablename,),
    )
    columns = [column[0] for column in cursor.fetchall()]

    global  data
    # 遍历 DataFrame 的每一行，将数据转换为插入语句所需的格式
    for index, row in df.iterrows():
        # 取row的0至45 加上224至245

        type_ = (type,)

        if type == 'kindergarten':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4])
        elif type == 'primary':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4]) + tuple(str(row[174])) + tuple(str(row[185]))
        elif type == 'middle':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4]) + tuple(str(row[199])) + tuple(str(row[210]))
        elif type == 'high':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4]) + tuple(str(row[175])) + tuple(str(row[186]))
        elif type == 'special':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4]) + (None,) + tuple(str(row[263]))
        elif type == 'vocational':
            data = type_ + tuple(row[index1:index2]) + tuple(row[index3:index4]) + (None,) + tuple(str(row[227]))

        # 下面这行代码的数字都减1
        # data = data[:2] + (str(data[2]),) + (data[3],) + (str(data[4]),) + data[5:8] + (str(data[8]),) + data[9:11] + (str(data[11]),) + data[12:27] + (str(data[27]),) + data[28:33] + (str(data[33]),) + data[34:43] + (str(data[43]),) + (str(data[44]),) + (data[45:])
        # data = data[:1] + (str(data[1]),) + (data[2],) + (str(data[3]),) + data[4:7] + (str(data[7]),) + data[8:10] + (str(data[10]),) + data[11:26] + (str(data[26]),) + data[27:32] + (str(data[32]),) + data[33:42] + (str(data[42]),) + (str(data[43]),) + data[44:]
        
        # tuple 第45至67 填充None
        data = data + (None,) * (len(columns) - len(data))
        # data[17]如果值是“是”，则转换为1，否则转换为0
        if data[18] == "是":
            data = data[:18] + (1,) + data[19:]
        else:
            data = data[:18] + (0,) + data[19:]

        # 第25列如果值是“无”，则转换为0，“非营利”否则转换为，“营利”转为2
        if data[25] == "无":
            data = data[:25] + (0,) + data[26:]
        elif data[25] == "非营利":
            data = data[:25] + (1,) + data[26:]
        else:
            data = data[:25] + (2,) + data[26:]

        # 第42列的值如果是nan转为''
        if pd.isna(data[42]):
            data = data[:42] + ("",) + data[43:]
        
        if data[59] == "是":
            data = data[:60] + (1,) + data[61:]
        else:
            data = data[:60] + (0,) + data[61:]
        
        #第67列转为0
        try:
            data_67 = int(data[67])
        except:
            data_67 = 0
        data = data[:67] + (data_67,) + data[68:]

        # 当前时间格式转为'%Y-%m-%d %H:%M:%S'并转成字符串类型
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = data[:68] + (now_time,) + (data[69],) + (now_time,) + data[71:]
        # 第 54，55，56 列替换'.0'为''
        data = data[:53] + (str(data[53]).replace('.0', ''),) + (str(data[54]).replace('.0', ''),) + (str(data[55]).replace('.0', ''),) + data[56:]

        # 所有字段的nan转为''
        data = tuple([None if str(x) == 'nan' else x for x in data])

        data_to_insert.append(data)

    # 构建插入语句，ID 自增
    insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (
        tablename,
        ", ".join(columns),
        ", ".join(["%s"] * len(columns)),
    )
    print(data_to_insert[-1])
    cursor.executemany(insert_sql, data_to_insert)

    conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":

    for file in dirs:
        param1 = 0
        param2 = 0
        param3 = 0
        param4 = 0
        type = ''
    
        if not file.endswith(".xlsx"):
            continue

        if "幼儿园" in file:
            param1 = 0
            param2 = 45
            param3 = 224
            param4 = 246
            type = 'kindergarten'

            # test_show_value(df)
        if "小学" in file:
            param1 = 0
            param2 = 45
            param3 = 147
            param4 = 167
            type = 'primary'

        if "初中" in file:
            param1 = 0
            param2 = 45
            param3 = 171
            param4 = 191
            type ='middle'

        if "高中" in file:
            param1 = 0
            param2 = 45
            param3 = 147
            param4 = 167
            type = 'high'

        if "特教" in file:
            param1 = 0
            param2 = 45
            param3 = 243
            param4 = 263
            type ='special'

        if "中等职业教育" in file:
            param1 = 0
            param2 = 45
            param3 = 194
            param4 = 214
            type ='vocational'
        
        df = pd.read_excel("E:\\workspaces\\2024\\10月\\需导入数据\\" + file)
        extract_data(df, tablename, param1, param2, param3, param4, type)
                