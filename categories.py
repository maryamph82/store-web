
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base() 

class Categories(base) : 
    __tablename__ = 'categories'

    category_id = Column('category_id' ,Integer, primary_key=True, autoincrement=True)
    category_name = Column('category_name',String)
