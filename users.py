
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base() 

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
    user_type = Column('user_type',String, default='User')
    password = Column('password' , String)
