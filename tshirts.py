
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from products import Products

base = declarative_base()

class Tshirts(base) : 
    __tablename__ = 'tshirts'

    tshirt_id = Column('tshirt_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")
