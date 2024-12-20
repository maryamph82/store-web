from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , Boolean , Float , DATE , DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_


# database + library://username:password@host:port/databasename
engine = create_engine("postgresql+psycopg2://maryam:123456@localhost:5432/store_system") # echo=True
base = declarative_base() # ساخت آبجکت
session = sessionmaker(bind=engine)() # برای بخش سلکت به درد میخوره  autocommit = True


class Student(base) : # از بیس ارث بری میکنه
    __tablename__ = 'student'
    _id = Column('id' , Integer , unique=True , primary_key=True)
    name = Column('name' , String(50))


base.metadata.create_all(engine)


#select
# students = session.query(Student).all()
# # print(students)
# for student in students :
#     print(student._id , student.name)

# students = session.query(Student).first()
# print(students._id , students.name)

# students = session.query(Student).filter(Student.name=='ali').all() # مثل شرط ور در دستورات اسکیول
# print(students)

# students = session.query(Student).filter(and_(Student.name=='reza' , Student._id==2)).all()
# print(students)

# students = session.query(Student).order_by(Student._id).all()
# print(students)


# insert
# student_1 = Student(name='mohammad') # ایدی اتوماتیک خودش در نظر میگیره
# session.add(student_1)
# session.commit()

# student_2 = Student(name='mohammadali') # ایدی اتوماتیک خودش در نظر میگیره
# student_3 = Student(name='mohammadreza')
# session.add_all([student_2,student_3])
# session.commit() اتوکامیت باشه دیگه نیازی به این کد نیست




# delete
# student = session.query(Student).filter(Student.name=='mohammadali').first()
# session.delete(student)
# session.commit()
# # دیلیت با سلکت از قبل

# student = session.query(Student).filter(Student.name=='mohammadreza').delete()
# session.commit() 
# # دیلیت مستقیم


# update
# session.query(Student).filter(Student.name=='mohammad').update({'name' : 'mamad'})
# session.commit()
# اپدیت مستقیم

student = session.query(Student).filter(Student.name=='mamad').first()
student.name = 'ali'
session.commit()
# اپدیت با سلکت از قبل


