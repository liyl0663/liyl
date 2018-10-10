from dbconn import Session,Department,Employee

seesion = Session()
query1 = seesion.query(Department)
print(query1)

for instance in query1:
    print(instance)

dep = query1[0]
print(dep)
print(dep.dep_id,dep.dep_name)


print('#' * 40)
query2 = seesion.query(Department).order_by(Department.dep_id)
print(query2)
for instance in query2:
    print(instance)
print('#' * 40)

query3 = seesion.query(Employee.emp_name,Employee.phone)
print(query3)
print(list(query3))
for name,phone in query3:
    print('%s:%s' % (name,phone))
print('#' * 40)

query4 = seesion.query(Department.dep_name.label('部门'))
print(query4)
for dep in query4:
    print(dep.部门)
print('#' * 40)

query5 = seesion.query(Department).order_by(Department.dep_id)[1:5]
print(query5)
for dep in query5:
    print(dep)
print('#' * 40)

query6  = seesion.query(Department).filter(Department.dep_id == 2)
print(query6)
for dep in query6:
    print(dep)

query7 = seesion.query(Department).filter(Department.dep_id > 2).filter(Department.dep_id<4)
print(query7)
for dep in query7:
    print(dep)
print('#' * 40)

query8 = seesion.query(Department).filter(Department.dep_id!=2)
print(query8)
for dep in query8:
    print(dep)
print('#' * 40)

query9 = seesion.query(Department).filter(Department.dep_name.like('%部'))
print(query9)
for dep in query9:
    print(dep)
print('#' * 40)

query10 = seesion.query(Department).filter(Department.dep_id.in_([1,3,4]))
print(query10)
for dep in query10:
    print(dep)
print('#' * 40)

query11 = seesion.query(Department).filter(~Department.dep_id.in_([1,3,4]))
print(query11)  # ~表示取反
for dep in query11:
    print(dep)
print('#' * 40)

query12 = seesion.query(Department).filter(Department.dep_name.is_(None))
print(query12)
for dep in query12:
    print(dep)
print('#' * 40)

query13 = seesion.query(Department).filter(Department.dep_name.isnot(None))
print(query13)
for dep in query13:
    print(dep)
print('#' * 40)

from sqlalchemy import and_, or_
query14 = seesion.query(Department)\
    .filter(and_(Department.dep_id>2, Department.dep_id<4))
print(query14)
for dep in query14:
    print(dep)
print('#' * 40)

query15 = seesion.query(Department)\
    .filter(or_(Department.dep_id<2, Department.dep_id>4))
print(query15)
for dep in query15:
    print(dep)


