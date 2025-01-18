from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, LargeBinary , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Boolean , Float , Date , DateTime , Enum ,  BLOB 
from sqlalchemy.orm import sessionmaker , relationship
from sqlalchemy.sql.expression import and_
from datetime import date
import os
import enum



engine = create_engine("postgresql+psycopg2://maryam:123456@localhost:5432/store_system")
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
    category = relationship("Categories")


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


user_1 = Users(postal_code='98765',address='tehran-zanbagh',first_name='Maryam',last_name='Rajabi',national_code='0765434567',phone_number='09362876434',birth_date=date(2000,7,7),user_type='Admin',password='75443') 
user_2 = Users(postal_code='12346',address='karaj-jahanshahr',first_name='Fatemeh',last_name='Saberi',national_code='0427335987',phone_number='09361543212',birth_date=date(2003,7,12),password='123')
user_3 = Users(postal_code='12347',address='karaj-baghestan',first_name='Asal',last_name='Haghzad',national_code='0365436744',phone_number='09123456789',birth_date=date(2005,8,26),password='5432')
user_4 = Users(postal_code='123439',address='karaj-mahdasht',first_name='Sara',last_name='Ghanbari',national_code='07634',phone_number='09365412134',birth_date=date(2003,4,25),password='85432')
user_5 = Users(postal_code='48769',address='tehran-khavaran',first_name='Ali',last_name='Rahimi',national_code='0873217655',phone_number='09012357249',birth_date=date(2000,7,30),password='17659')
# session.add_all([user_1,user_2,user_3,user_4,user_5])


category_1 = Categories(category_name='bag') 
category_2 = Categories(category_name='belt')
category_3 = Categories(category_name='coat')
category_4 = Categories(category_name='hat')
category_5 = Categories(category_name='hoody')
category_6 = Categories(category_name='pant')
category_7 = Categories(category_name='scarf')
category_8 = Categories(category_name='shoes')
category_9 = Categories(category_name='skirt')
category_10 = Categories(category_name='sock')
category_11 = Categories(category_name='tshirt')
# session.add_all([category_1,category_2,category_3,category_4,category_5,category_6,category_7,category_8,category_9,category_10,category_11])


category_instance = session.query(Categories).filter(Categories.category_id == 341).one()

new_product = Products(name='Men\'s T-shirt',color='blue',quantity=50,category=category_instance,gender=GenderEnum.male,brand='Nike',material='cotton',date=date(2024,7,1),picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/تیشرت مردانه.jpg','rb').read(),price=50000)  
# session.add(new_product)

category_instance1 = session.query(Categories).filter(Categories.category_id == 331).one()
category_instance2 = session.query(Categories).filter(Categories.category_id == 332).one()
category_instance3 = session.query(Categories).filter(Categories.category_id == 333).one()
category_instance4 = session.query(Categories).filter(Categories.category_id == 334).one()
category_instance5 = session.query(Categories).filter(Categories.category_id == 335).one()
category_instance6 = session.query(Categories).filter(Categories.category_id == 336).one()
category_instance7 = session.query(Categories).filter(Categories.category_id == 337).one()
category_instance8 = session.query(Categories).filter(Categories.category_id == 338).one()
category_instance9 = session.query(Categories).filter(Categories.category_id == 339).one()
category_instance10 = session.query(Categories).filter(Categories.category_id == 340).one()
category_instance11 = session.query(Categories).filter(Categories.category_id == 341).one()


product_1 = Products(name='handbag', color='brown', quantity=20, category=category_instance1, gender=GenderEnum.female, brand='Gucci', material='leather', date=date(2024, 7, 1), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کیف-برند-گوچی-2-min-1.jpg', 'rb').read(), price=150000)
product_2 = Products(name='belt', color='black', quantity=50, category=category_instance2, gender=GenderEnum.male, brand='Levi\'s', material='leather', date=date(2024, 7, 2), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کمربند مشکی.jpg', 'rb').read(), price=30000)
product_3 = Products(name='winter coat', color='white', quantity=15, category=category_instance3, gender=GenderEnum.male, brand='Zara', material='wool', date=date(2024, 7, 3), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کت زمستانی سفید.jpg', 'rb').read(), price=500000)
product_4 = Products(name='hat', color='red', quantity=25, category=category_instance4, gender=GenderEnum.female, brand='Adidas', material='cotton', date=date(2024, 7, 4), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کلاه قرمز آدیداس.jpg', 'rb').read(), price=25000)
product_5 = Products(name='hoodie', color='grey', quantity=30, category=category_instance5, gender=GenderEnum.male, brand='Nike', material='polyester', date=date(2024, 7, 5), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/هودی خاکستری نایک.jpg', 'rb').read(), price=120000)
product_6 = Products(name='pants', color='blue', quantity=40, category=category_instance6, gender=GenderEnum.female, brand='H&M', material='jane', date=date(2024, 7, 6), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/شلوار آبی جین.jpg', 'rb').read(), price=80000)
product_7 = Products(name='shawl', color='yellow', quantity=35, category=category_instance7, gender=GenderEnum.female, brand='Hermès', material='silk', date=date(2024, 7, 7), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/شال زرد هرمس.jpg', 'rb').read(), price=200000)
product_8 = Products(name='shoes', color='white', quantity=45, category=category_instance8, gender=GenderEnum.male, brand='Reebok', material='leather', date=date(2024, 7, 8), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کفش سفید ریبوک.jpg', 'rb').read(), price=180000)
product_9 = Products(name='skirt', color='pink', quantity=20, category=category_instance9, gender=GenderEnum.female, brand='Versace', material='wool', date=date(2024, 7, 9), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/دامن صورتی پشمی.jpg', 'rb').read(), price=250000)
product_10 = Products(name='socks', color='white', quantity=100, category=category_instance10, gender=GenderEnum.female, brand='Nike', material='cotton', date=date(2024, 7, 15), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/جوراب سفید نایک.jpg', 'rb').read(), price=5000)
product_11 = Products(name='T-shirt', color='red', quantity=60, category=category_instance11, gender=GenderEnum.male, brand='Adidas', material='cotton', date=date(2024, 7, 20), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/تیشرت آدیداس قرمز.jpg', 'rb').read(), price=40000)

# session.add_all([product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10, product_11])

product_instance1 = session.query(Products).filter(Products.product_id == 17).one()
coat_1 = Coats(product=product_instance1 , size='Large' , description='A great winter coat') 
# session.add(coat_1)

product_instance2 = session.query(Products).filter(Products.product_id == 15).one()
bag_1 = Bags(product=product_instance2 , description='A handbag with excellent quality and medium size') 
# session.add(bag_1)

product_instance3 = session.query(Products).filter(Products.product_id == 24).one()
socks_1 = Socks(product=product_instance3 , description='simple-Medium') 
# 'ساده-بزرگ'
# 'طرح دار-کوچک'
# 'خال خالی-کوچک'
# 'راه راه-متوسط'
# session.add(socks_1)

product_instance4 = session.query(Products).filter(Products.product_id == 21).one()
scarf_1 = Scarves(product=product_instance4 , description='crowded design farm-suitable for autumn season') 
# session.add(scarf_1)

product_instance5 = session.query(Products).filter(Products.product_id == 22).one()
shoes_1 = Shoes(product=product_instance5 ,size='37' , description='A sport shoes without legs') 
# session.add(shoes_1)

product_instance6 = session.query(Products).filter(Products.product_id == 14).one()
product_instance7 = session.query(Products).filter(Products.product_id == 25).one()
tshirt_1 = Tshirts(product=product_instance6 ,size='Large' , description='A high quality blue Nike t-shirt') 
tshirt_2 = Tshirts(product=product_instance7 ,size='Small' , description='A high quality red adidas t-shirt')
# session.add_all([tshirt_1,tshirt_2])

product_instance8 = session.query(Products).filter(Products.product_id == 19).one()
hoodie_1 = Hoodies(product=product_instance8 ,size='Large',with_hood=True ,description='A high quality and comfortable gray Nike hooded sweatshirt') 
# session.add(hoodie_1)

product_instance9 = session.query(Products).filter(Products.product_id == 16).one()
belt_1 = Belts(product=product_instance9 ,description='A classic formal black belt with a metal buckle and rectangular hole design with a width of 3.5 and a medium size') 
# session.add(belt_1)

product_instance10 = session.query(Products).filter(Products.product_id == 20).one()
pant_1 = Pants(product=product_instance10 ,size='32' , description='A blue jeans with a modern and comfortable design and suitable for everyday use') 
# session.add(pant_1)

product_instance24 = session.query(Products).filter(Products.product_id == 18).one()
hat_1 = Hats(product=product_instance24 ,description='A high quality red adidas cap suitable for everyday use and sports activities') 
# session.add(hat_1)


user_instance2 = session.query(Users).filter(Users.user_id == 183).one() 
product_instance12 = session.query(Products).filter(Products.product_id == 15).one()
product_instance13 = session.query(Products).filter(Products.product_id == 17).one()
product_instance14 = session.query(Products).filter(Products.product_id == 18).one()
user_instance3 = session.query(Users).filter(Users.user_id == 184).one() 
product_instance15 = session.query(Products).filter(Products.product_id == 20).one()
product_instance16 = session.query(Products).filter(Products.product_id == 23).one()
user_instance4 = session.query(Users).filter(Users.user_id == 185).one() 
product_instance17 = session.query(Products).filter(Products.product_id == 21).one()
user_instance5 = session.query(Users).filter(Users.user_id == 186).one() 
product_instance18 = session.query(Products).filter(Products.product_id == 22).one()
product_instance19 = session.query(Products).filter(Products.product_id == 24).one()
product_instance20 = session.query(Products).filter(Products.product_id == 25).one()
user_instance6 = session.query(Users).filter(Users.user_id == 187).one() 
product_instance21 = session.query(Products).filter(Products.product_id == 14).one()
product_instance22 = session.query(Products).filter(Products.product_id == 16).one()
product_instance23 = session.query(Products).filter(Products.product_id == 19).one()

order_1 = Orders(product=product_instance12 ,user=user_instance2 ,order_date=date(2024,8,1) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_2 = Orders(product=product_instance13 ,user=user_instance2 ,order_date=date(2024,10,23) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_3 = Orders(product=product_instance14 ,user=user_instance2 ,order_date=date(2024,9,20) ,payment_method='Gift card' ,order_status=True ,quantity=1 )
order_4 = Orders(product=product_instance15 ,user=user_instance3 ,order_date=date(2024,8,30) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_5 = Orders(product=product_instance16 ,user=user_instance3 ,order_date=date(2025,1,1) ,payment_method='Payment on the spot' ,order_status=False ,quantity=1 )
order_6 = Orders(product=product_instance17 ,user=user_instance4 ,order_date=date(2024,12,14) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_7 = Orders(product=product_instance18 ,user=user_instance5 ,order_date=date(2024,11,22) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_8 = Orders(product=product_instance19 ,user=user_instance5 ,order_date=date(2025,1,5) ,payment_method='Gift card' ,order_status=True ,quantity=1 )
order_9 = Orders(product=product_instance20 ,user=user_instance5 ,order_date=date(2024,8,3) ,payment_method='Online payment' ,order_status=False ,quantity=1 )
order_10 = Orders(product=product_instance21 ,user=user_instance6 ,order_date=date(2024,8,4) ,payment_method='Online payment' ,order_status=True ,quantity=1 )
order_11 = Orders(product=product_instance22 ,user=user_instance6 ,order_date=date(2024,11,13) ,payment_method='Gift card' ,order_status=True ,quantity=1 )
order_12 = Orders(product=product_instance23 ,user=user_instance6 ,order_date=date(2024,8,16) ,payment_method='Payment on the spot' ,order_status=True ,quantity=1 )
# session.add_all([order_1,order_2,order_3,order_4,order_5,order_6,order_7,order_8,order_9,order_10,order_11,order_12])

product_instance24 = session.query(Products).filter(Products.product_id == 23).one()
skirt_1 = Skirts(product=product_instance24 ,size='Medium' , description='Safe pink Versace to the knee') 
session.add(skirt_1)

session.commit()
session.close()

    
