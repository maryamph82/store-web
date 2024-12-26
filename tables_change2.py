from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , Boolean , Float , Date , DateTime , Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_
from datetime import date



engine = create_engine("postgresql+psycopg2://maryam:123456@localhost:5432/store_system")
base = declarative_base() 

# class User_type(Enum) :
#     user = 'user'
#     admin = 'admin'

class Users(base) : 
    __tablename__ = 'users'

    user_id = Column('user_id' ,Integer, primary_key=True, autoincrement=True)
    postal_code = Column('postal_code',String)
    address = Column('address',String)
    first_name = Column('first_name',String(50))
    last_name = Column('last_name',String)
    national_code = Column('national_code',String)
    phone_number = Column('phone_number',String)
    birth_date = Column('birth_date',Date)
    user_type = Column('user_type',String, default='user')
    password = Column('password' , String)



session = sessionmaker(bind=engine)()

base.metadata.create_all(engine)




user_1 = Users(postal_code='48769',address='tehran-khavaran',first_name='Ali',last_name='Rahimi',national_code='0873217655',phone_number='09012357249',birth_date=date(2000,7,30),password='17659') 
# user_2 = Users(postal_code='12346',address='karaj-jahanshahr',first_name='Fatemeh',last_name='Saberi',national_code='0427335987',phone_number='09361543212',birth_date=date(2003,7,12),password='123')
# user_3 = Users(postal_code='12347',address='karaj-baghestan',first_name='Asal',last_name='Haghzad',national_code='0365436744',phone_number='09123456789',birth_date=date(2005,8,26),password='5432')
# user_4 = Users(postal_code='123439',address='karaj-mahdasht',first_name='Sara',last_name='Ghanbari',national_code='07634',phone_number='09365412134',birth_date=date(2003,4,25),password='85432')
session.add_all([user_1])

session.commit()
session.close()

    
