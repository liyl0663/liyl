import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'tarena1804',
    charset = 'utf8'
)

youbiao = conn.cursor()
insert1 = 'INSERT INTO department VALUES (%s,%s)'
result1 = youbiao.execute(insert1,(5,'财务部'))
conn.commit()
youbiao.close()
conn.close()