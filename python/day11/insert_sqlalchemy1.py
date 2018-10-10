from dbconn import Department,Session,Employee,Salary

session = Session()
dep_dev = Department(dep_name='development')
dep_hr = Department(dep_name='人事部')
dep_op = Department(dep_name='运维部')
# session.add_all([dep_hr,dep_op])
#session.add(dep_dev)
my = Employee(
    emp_name = '马云',
    gender =  'malse',
    birth_date = '1991-01-02',
    phone = '15988663322',
    email = 'my@taobao.com',
    dep_id = 3
)
mht = Employee(
    emp_name = '马化腾',
    gender =  'malse',
    birth_date = '1991-05-02',
    phone = '15988776655',
    email = 'mht@tencent.com',
    dep_id = 3
)
lyh = Employee(
    emp_name = '李彦宏',
    gender =  'malse',
    birth_date = '1991-06-02',
    phone = '15999886655',
    email = 'lyh@baidu.com',
    dep_id = 3
)



my201810 = Salary(emp_id=1,date='2018-10-01',basic=15000,awards=5000)
session.add(my201810)

#session.add_all([my,mht,lyh])
session.commit()
session.close()
