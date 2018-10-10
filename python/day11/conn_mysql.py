import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tarena1804',
    charset = 'utf8'
)
cursor = conn.cursor()


# insert1 = 'insert into department values (%s,%s)'
# result1 = cursor.execute(insert1,(1,'development'))
# depts1 = [(2,'operations'),(3,'QA')]
# depts2 = [(4,'人事部'),(5,'财务部')]
# result2 = cursor.executemany(insert1,depts1)
# result3 = cursor.executemany(insert1,depts2)
# conn.commit()
# cursor.close()
# conn.close()

# query1 = 'select * from department'
# cursor.execute(query1)
# data1 = cursor.fetchone()
# #data1 = cursor.fetchall()
# print(data1)
# data2 = cursor.fetchmany(2)
# data3 = cursor.fetchall()
# print(data2)
# print(data3)

# query1 = 'select * from department'
# cursor.execute(query1)
# cursor.scroll(1,'absolute')
# data1 = cursor.fetchone()
# print(data1)
# cursor.scroll(2)
# data2 = cursor.fetchone()
# print(data2)
update1 = 'update department set dep_name=%s where dep_name=%s'
data1 = cursor.execute(update1,('人事部','人力资源部'))
print(data1)
delete1 = 'delete from department where dep_id=%s'
cursor.execute(delete1,5)
conn.commit()
cursor.close()
conn.close()
