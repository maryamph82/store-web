
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from products import Products

base = declarative_base()

class Hoodies(base) : 
    __tablename__ = 'hoodies'

    hoodie_id = Column('hoodie_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    with_hood = Column('with_hood',Boolean)
    description = Column('description',String)
    product = relationship("Products")
