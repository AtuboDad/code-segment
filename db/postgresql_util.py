import psycopg2
import datetime

host = '192.168.131.128'
user ='postgres'
password ='postgres'
dbname ='postgres'
port ='5432'

tablename ='edu_test'
# 连接到数据库

def connect():
    conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname, port=port)
    return conn

def test_connect():
    conn = connect()

    # 创建一个游标对象
    cur = conn.cursor()
    # 执行查询
    cur.execute("SELECT * FROM %s" % tablename)
    # 获取查询结果
    rows = cur.fetchall()
    # 处理结果
    for row in rows:
        print(row)
    # 关闭游标和连接
    cur.close()
    conn.close()

def test_add():
    conn = connect()
    cur = conn.cursor()
    # 查询表中所有列名，按照其在表中的顺序排列

    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = %s AND column_name <> 'id' ORDER BY ordinal_position", (tablename,))
    columns = [column[0] for column in cur.fetchall()]
    # 构建插入语句
    insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (tablename, ', '.join(columns), ', '.join(['%s'] * len(columns)))
    print(insert_sql)

    # 设置当前时间格式为2023-03-03 12:34:56
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 构建插入数据
    data = ('测试数据3', now, 'admin', None, None, 1)
    # 执行插入语句
    cur.execute(insert_sql, data)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    # test_connect()
    test_add()