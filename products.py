
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, LargeBinary, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

base = declarative_base() 

class GenderEnum(enum.Enum): 
    male = "مردانه" 
    female = "زنانه" 
    child = "بچگانه"


class Products(base) : 
    __tablename__ = 'products'

    product_id = Column('product_id' ,Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    color = Column('color',String)
    quantity = Column('quantity',Integer)
    category_id = Column('category_id',Integer, ForeignKey('categories.category_id'))
    gender = Column('gender', Enum(GenderEnum))
    brand = Column('brand',String)
    material = Column('material',String)
    date = Column('date',Date)
    picture = Column('picture', LargeBinary )
    price = Column('price',Float)
    category = relationship("Categories")
