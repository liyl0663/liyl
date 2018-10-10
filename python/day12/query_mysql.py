import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='tarena1804',
    charset='utf8'
)

cursor = conn.cursor()
query1 = 'select * from department'
cursor.execute(query1)
# data1 = cursor.fetchone()
# print(data1)
#
# data2 = cursor.fetchmany(3)
# print(data2)

data3 = cursor.fetchall()
print(data3)