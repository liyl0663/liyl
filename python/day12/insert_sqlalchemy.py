from dbconn import  Department,Student,Session

session = Session()
dep_hr = Department(dep_name='人事部')
dep_op = Department(dep_name='运维部')
dep_fn = Department(dep_id=3,dep_name='财务部')
session.add(dep_fn)
# session.add_all([dep_hr,dep_op])


session.commit()
session.close()
