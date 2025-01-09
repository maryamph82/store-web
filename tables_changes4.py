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
    user_id = Column('user_id',Integer, ForeignKey('users.user_id'))
    category_id = Column('category_id',Integer, ForeignKey('categories.category_id'))
    gender = Column('gender', Enum(GenderEnum))
    brand = Column('brand',String)
    material = Column('material',String)
    date = Column('date',Date)
    picture = Column('picture', LargeBinary )
    price = Column('price',Float)
    category = relationship("Categories")
    user = relationship("Users")


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


user_instance = session.query(Users).filter(Users.user_id == 182).one() 
category_instance = session.query(Categories).filter(Categories.category_id == 319).one()

new_product = Products(name='تیشرت مردانه',color='آبی',quantity=50,user=user_instance,category=category_instance,gender=GenderEnum.male,brand='Nike',material='نخی',date=date(2024,7,1),picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/تیشرت مردانه.jpg','rb').read(),price=50000)  
# session.add(new_product)

user_instance1 = session.query(Users).filter(Users.user_id == 179).one()
user_instance2 = session.query(Users).filter(Users.user_id == 182).one()
user_instance3 = session.query(Users).filter(Users.user_id == 182).one()
user_instance4 = session.query(Users).filter(Users.user_id == 181).one()
user_instance5 = session.query(Users).filter(Users.user_id == 181).one()
user_instance6 = session.query(Users).filter(Users.user_id == 180).one()
user_instance7 = session.query(Users).filter(Users.user_id == 178).one()
user_instance8 = session.query(Users).filter(Users.user_id == 178).one()
user_instance9 = session.query(Users).filter(Users.user_id == 181).one()
user_instance10 = session.query(Users).filter(Users.user_id == 179).one()
user_instance11 = session.query(Users).filter(Users.user_id == 178).one()

category_instance1 = session.query(Categories).filter(Categories.category_id == 309).one()
category_instance2 = session.query(Categories).filter(Categories.category_id == 310).one()
category_instance3 = session.query(Categories).filter(Categories.category_id == 311).one()
category_instance4 = session.query(Categories).filter(Categories.category_id == 312).one()
category_instance5 = session.query(Categories).filter(Categories.category_id == 313).one()
category_instance6 = session.query(Categories).filter(Categories.category_id == 314).one()
category_instance7 = session.query(Categories).filter(Categories.category_id == 315).one()
category_instance8 = session.query(Categories).filter(Categories.category_id == 316).one()
category_instance9 = session.query(Categories).filter(Categories.category_id == 317).one()
category_instance10 = session.query(Categories).filter(Categories.category_id == 318).one()
category_instance11 = session.query(Categories).filter(Categories.category_id == 319).one()


product_1 = Products(name='کیف دستی', color='قهوه‌ای', quantity=20, user=user_instance1, category=category_instance1, gender=GenderEnum.female, brand='Gucci', material='چرم', date=date(2024, 7, 1), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کیف-برند-گوچی-2-min-1.jpg', 'rb').read(), price=150000)
product_2 = Products(name='کمربند', color='مشکی', quantity=50, user=user_instance2, category=category_instance2, gender=GenderEnum.male, brand='Levi\'s', material='چرم', date=date(2024, 7, 2), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کمربند مشکی.jpg', 'rb').read(), price=30000)
product_3 = Products(name='کت زمستانی', color='سفید', quantity=15, user=user_instance3, category=category_instance3, gender=GenderEnum.male, brand='Zara', material='پشم', date=date(2024, 7, 3), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کت زمستانی سفید.jpg', 'rb').read(), price=500000)
product_4 = Products(name='کلاه', color='قرمز', quantity=25, user=user_instance4, category=category_instance4, gender=GenderEnum.female, brand='Adidas', material='پنبه', date=date(2024, 7, 4), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کلاه قرمز آدیداس.jpg', 'rb').read(), price=25000)
product_5 = Products(name='هودی', color='خاکستری', quantity=30, user=user_instance5, category=category_instance5, gender=GenderEnum.male, brand='Nike', material='پلی‌استر', date=date(2024, 7, 5), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/هودی خاکستری نایک.jpg', 'rb').read(), price=120000)
product_6 = Products(name='شلوار', color='آبی', quantity=40, user=user_instance6, category=category_instance6, gender=GenderEnum.female, brand='H&M', material='جین', date=date(2024, 7, 6), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/شلوار آبی جین.jpg', 'rb').read(), price=80000)
product_7 = Products(name='شال', color='زرد', quantity=35, user=user_instance7, category=category_instance7, gender=GenderEnum.female, brand='Hermès', material='ابریشم', date=date(2024, 7, 7), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/شال زرد هرمس.jpg', 'rb').read(), price=200000)
product_8 = Products(name='کفش', color='سفید', quantity=45, user=user_instance8, category=category_instance8, gender=GenderEnum.male, brand='Reebok', material='چرم', date=date(2024, 7, 8), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/کفش سفید ریبوک.jpg', 'rb').read(), price=180000)
product_9 = Products(name='دامن', color='صورتی', quantity=20, user=user_instance9, category=category_instance9, gender=GenderEnum.female, brand='Versace', material='پشم', date=date(2024, 7, 9), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/دامن صورتی پشمی.jpg', 'rb').read(), price=250000)
product_10 = Products(name='جوراب', color='سفید', quantity=100, user=user_instance10, category=category_instance10, gender=GenderEnum.female, brand='Nike', material='پنبه', date=date(2024, 7, 15), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/جوراب سفید نایک.jpg', 'rb').read(), price=5000)
product_11 = Products(name='تیشرت', color='قرمز', quantity=60, user=user_instance11, category=category_instance11, gender=GenderEnum.male, brand='Adidas', material='پنبه', date=date(2024, 7, 20), picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/تیشرت آدیداس قرمز.jpg', 'rb').read(), price=40000)

# session.add_all([product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10, product_11])

product_instance1 = session.query(Products).filter(Products.product_id == 4).one()
coat_1 = Coats(product=product_instance1 , size='Large' , description='یک کت زمستانی عالی') 
# session.add(coat_1)

product_instance2 = session.query(Products).filter(Products.product_id == 2).one()
bag_1 = Bags(product=product_instance2 , description='یک کیف دستی با کیفیت عالی و سایز Medium') 
# session.add(bag_1)

product_instance3 = session.query(Products).filter(Products.product_id == 11).one()
socks_1 = Socks(product=product_instance3 , description='ساده-Medium') 
# 'ساده-بزرگ'
# 'طرح دار-کوچک'
# 'خال خالی-کوچک'
# 'راه راه-متوسط'
# session.add(socks_1)

product_instance4 = session.query(Products).filter(Products.product_id == 8).one()
scarf_1 = Scarves(product=product_instance4 , description='چارخانه طرح شلوغ-مناسب فصل پاییز') 
# session.add(scarf_1)

product_instance5 = session.query(Products).filter(Products.product_id == 9).one()
shoes_1 = Shoes(product=product_instance5 ,size='37' , description='یک کتونی اسپرت بدون ساق') 
# session.add(shoes_1)

product_instance6 = session.query(Products).filter(Products.product_id == 1).one()
product_instance7 = session.query(Products).filter(Products.product_id == 12).one()
tshirt_1 = Tshirts(product=product_instance6 ,size='Large' , description='یک تیشرت نایک آبی با کیفیت بالا') 
tshirt_2 = Tshirts(product=product_instance7 ,size='Small' , description='یک تیشرت آدیداس قرمز با کیفیت بالا')
# session.add_all([tshirt_1,tshirt_2])

product_instance8 = session.query(Products).filter(Products.product_id == 6).one()
hoodie_1 = Hoodies(product=product_instance8 ,size='Large',with_hood=True ,description='یک هودی خاکستری کلاه دار نایک با کیفیت بالا و راحت') 
# session.add(hoodie_1)

product_instance9 = session.query(Products).filter(Products.product_id == 3).one()
belt_1 = Belts(product=product_instance9 ,description='یک کمربند مشکی و رسمی کلاسیک با سگک فلزی و طراحی سوراخ‌های مستطیلی و با عرض 3.5 و سایز Medium') 
# session.add(belt_1)

product_instance10 = session.query(Products).filter(Products.product_id == 7).one()
pant_1 = Pants(product=product_instance10 ,size='32' , description='یک شلوار جین آبی با طراحی مدرن و راحت-مناسب برای استفاده روزمره') 
# session.add(pant_1)

product_instance11 = session.query(Products).filter(Products.product_id == 10).one()
skirt_1 = Skirts(product=product_instance11 ,size='Medium' , description='یک دامن صورتی پشمی با طرح گل‌دار زیبا و طول زیر زانو مناسب خانه') 
# session.add(skirt_1)

product_instance24 = session.query(Products).filter(Products.product_id == 5).one()
hat_1 = Hats(product=product_instance24 ,description='یک کلاه قرمز آدیداس با کیفیت بالا-مناسب برای استفاده روزانه و فعالیت‌های ورزشی') 
# session.add(hat_1)


user_instance2 = session.query(Users).filter(Users.user_id == 178).one() 
product_instance12 = session.query(Products).filter(Products.product_id == 8).one()
product_instance13 = session.query(Products).filter(Products.product_id == 9).one()
product_instance14 = session.query(Products).filter(Products.product_id == 12).one()
user_instance3 = session.query(Users).filter(Users.user_id == 179).one() 
product_instance15 = session.query(Products).filter(Products.product_id == 2).one()
product_instance16 = session.query(Products).filter(Products.product_id == 11).one()
user_instance4 = session.query(Users).filter(Users.user_id == 180).one() 
product_instance17 = session.query(Products).filter(Products.product_id == 7).one()
user_instance5 = session.query(Users).filter(Users.user_id == 181).one() 
product_instance18 = session.query(Products).filter(Products.product_id == 5).one()
product_instance19 = session.query(Products).filter(Products.product_id == 6).one()
product_instance20 = session.query(Products).filter(Products.product_id == 10).one()
user_instance6 = session.query(Users).filter(Users.user_id == 182).one() 
product_instance21 = session.query(Products).filter(Products.product_id == 1).one()
product_instance22 = session.query(Products).filter(Products.product_id == 3).one()
product_instance23 = session.query(Products).filter(Products.product_id == 4).one()

order_1 = Orders(product=product_instance12 ,user=user_instance2 ,order_date=date(2024,8,1) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_2 = Orders(product=product_instance13 ,user=user_instance2 ,order_date=date(2024,10,23) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_3 = Orders(product=product_instance14 ,user=user_instance2 ,order_date=date(2024,9,20) ,payment_method='کارت هدیه یا ووچر' ,order_status=True ,quantity=1 )
order_4 = Orders(product=product_instance15 ,user=user_instance3 ,order_date=date(2024,8,30) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_5 = Orders(product=product_instance16 ,user=user_instance3 ,order_date=date(2025,1,1) ,payment_method='پرداخت در محل' ,order_status=False ,quantity=1 )
order_6 = Orders(product=product_instance17 ,user=user_instance4 ,order_date=date(2024,12,14) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_7 = Orders(product=product_instance18 ,user=user_instance5 ,order_date=date(2024,11,22) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_8 = Orders(product=product_instance19 ,user=user_instance5 ,order_date=date(2025,1,5) ,payment_method='کارت هدیه یا ووچر' ,order_status=True ,quantity=1 )
order_9 = Orders(product=product_instance20 ,user=user_instance5 ,order_date=date(2024,8,3) ,payment_method='پرداخت آنلاین' ,order_status=False ,quantity=1 )
order_10 = Orders(product=product_instance21 ,user=user_instance6 ,order_date=date(2024,8,4) ,payment_method='پرداخت آنلاین' ,order_status=True ,quantity=1 )
order_11 = Orders(product=product_instance22 ,user=user_instance6 ,order_date=date(2024,11,13) ,payment_method='کارت هدیه یا ووچر' ,order_status=True ,quantity=1 )
order_12 = Orders(product=product_instance23 ,user=user_instance6 ,order_date=date(2024,8,16) ,payment_method='پرداخت در محل' ,order_status=True ,quantity=1 )
# session.add_all([order_1,order_2,order_3,order_4,order_5,order_6,order_7,order_8,order_9,order_10,order_11,order_12])

session.commit()
session.close()

    
