import pymysql

def outdata():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "lianjia")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM CS_ALL_LIANJIA"
    f = open('./out.csv', 'w', encoding='UTF-8')
    file=[]
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            size = row[4]
            numbers = row[3]
            rent = row[7]
            dist = row[9]
            # 打印结果
            f.write('"%s","%s","%s","%s"\n'%(size, numbers, rent, dist))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    f.close()


#outdata()