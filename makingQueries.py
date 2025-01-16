from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, LargeBinary , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Boolean , Float , Date , DateTime , Enum ,  BLOB 
from sqlalchemy.orm import sessionmaker , relationship
from sqlalchemy.sql.expression import and_
from datetime import date
import enum
from sqlalchemy import func
from datetime import datetime


engine = create_engine("postgresql+psycopg2://maryam:123456@78.38.35.219:5432/store_system")
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


class Categories(base) : 
    __tablename__ = 'categories'

    category_id = Column('category_id' ,Integer, primary_key=True, autoincrement=True)
    category_name = Column('category_name',String)


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
    category = relationship("Categories", backref="products")


class Coats(base) : 
    __tablename__ = 'coats'

    coat_id = Column('coat_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")


class Bags(base) : 
    __tablename__ = 'bags'

    bag_id = Column('bag_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")


class Socks(base) : 
    __tablename__ = 'socks'

    sock_id = Column('sock_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")

class Scarves(base) : 
    __tablename__ = 'scarves'

    scarf_id = Column('scarf_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")

class Shoes(base) : 
    __tablename__ = 'shoes'

    shoe_id = Column('shoe_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")

class Tshirts(base) : 
    __tablename__ = 'tshirts'

    tshirt_id = Column('tshirt_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")

class Hoodies(base) : 
    __tablename__ = 'hoodies'

    hoodie_id = Column('hoodie_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    with_hood = Column('with_hood',Boolean)
    description = Column('description',String)
    product = relationship("Products")

class Belts(base) : 
    __tablename__ = 'belts'

    belt_id = Column('belt_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")

class Pants(base) : 
    __tablename__ = 'pants'

    pant_id = Column('pant_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")

class Skirts(base) : 
    __tablename__ = 'skirts'

    skirt_id = Column('skirt_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    size = Column('size',String)
    description = Column('description',String)
    product = relationship("Products")

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

class Hats(base) : 
    __tablename__ = 'hats'

    hat_id = Column('hat_id' ,Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id',Integer,ForeignKey('products.product_id'))
    description = Column('description',String)
    product = relationship("Products")

session = sessionmaker(bind=engine)()
base.metadata.create_all(engine)


newest_products = session.query(Products).order_by(Products.date.desc()).limit(5).all()

for product in newest_products:
    print(f"ID : {product.product_id}")
    print(f"Name : {product.name}")
    print(f"Color: {product.color}")
    print(f"Quantity: {product.quantity}")
    print(f"Gender : {product.gender}")
    print(f"Brand : {product.brand}")
    print(f"Material : {product.material}")
    print(f"Date : {product.date}")
    # print(f"Picture : {product.picture}")
    print(f"Price : {product.price}")
    print(f"Category : {product.category.category_name}")
    print("----------------------------------------")


popular_brands = session.query(
    Products.brand,
    func.count(Orders.order_id).label('order_count')
).join(Orders, Products.product_id == Orders.product_id
).group_by(Products.brand
).order_by(func.count(Orders.order_id).desc()
).limit(5).all()

print("5 popular brands : ")
for brand, count in popular_brands:
    print(f"Brand: {brand}, Order Count: {count}")



session.commit()
session.close()

    
