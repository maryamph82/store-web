
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from products import Products

base = declarative_base()

class Bags(base) : 
    __tablename__ = 'bags'

    bag_id = Column('bag_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")
