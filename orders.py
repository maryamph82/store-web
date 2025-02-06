
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from products import Products
from users import Users

base = declarative_base()

class Orders(base) : 
    __tablename__ = 'orders'

    order_id = Column('order_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    user_id = Column('user_id',Integer,ForeignKey('users.user_id'))
    order_date= Column('order_date',Date)
    payment_method = Column('payment_method',String)
    order_status = Column('order_status',Boolean)
    quantity = Column('quantity',Integer)
    product = relationship("Products")
    user = relationship("Users")
