from sqlalchemy import create_engine,Column,Integer,String,Date,ForeignKey
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/tedu1804?charset=utf8',
    encoding = 'utf8',
    echo=True
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Department(Base):
    __tablename__  = 'department'
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True,nullable=False)

    # def __str__(self):
    #     return '<部门:%s>' % self.__tablename__

class Employee(Base):
    __tablename__ = 'employee'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20),nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    phone = Column(String(11),unique=True)
    email = Column(String(50),unique=True)
    dep_id = Column(Integer,ForeignKey('department.dep_id'))

    def __str__(self):
        return '<员工:%s>' % self.emp_name

class Salary(Base):
    __tablename__ = 'salary'
    autoid = Column(Integer,primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer,ForeignKey('employee.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)