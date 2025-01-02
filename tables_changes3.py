from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, LargeBinary , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Boolean , Float , Date , DateTime , Enum ,  BLOB
from sqlalchemy.orm import sessionmaker , relationship
from sqlalchemy.sql.expression import and_
from datetime import date


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


class Products(base) : 
    __tablename__ = 'products'

    product_id = Column('product_id' ,Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    color = Column('color',String)
    quantity = Column('quantity',Integer)
    user_id = Column('user_id',Integer, ForeignKey('users.user_id'))
    category_id = Column('category_id',Integer, ForeignKey('categories.category_id'))
    gender = Column('gender',String)
    brand = Column('brand',String)
    material = Column('material',String)
    date = Column('date',Date)
    picture = Column('picture', LargeBinary )
    price = Column('price',Float)
    category = relationship("Categories")
    user = relationship("Users")


session = sessionmaker(bind=engine)()
base.metadata.create_all(engine)


user_1 = Users(postal_code='98765',address='tehran-zanbagh',first_name='Maryam',last_name='Rajabi',national_code='0765434567',phone_number='09362876434',birth_date=date(2000,7,7),user_type='Admin',password='75443') 
user_2 = Users(postal_code='12346',address='karaj-jahanshahr',first_name='Fatemeh',last_name='Saberi',national_code='0427335987',phone_number='09361543212',birth_date=date(2003,7,12),password='123')
user_3 = Users(postal_code='12347',address='karaj-baghestan',first_name='Asal',last_name='Haghzad',national_code='0365436744',phone_number='09123456789',birth_date=date(2005,8,26),password='5432')
user_4 = Users(postal_code='123439',address='karaj-mahdasht',first_name='Sara',last_name='Ghanbari',national_code='07634',phone_number='09365412134',birth_date=date(2003,4,25),password='85432')
user_5 = Users(postal_code='48769',address='tehran-khavaran',first_name='Ali',last_name='Rahimi',national_code='0873217655',phone_number='09012357249',birth_date=date(2000,7,30),password='17659')
session.add_all([user_1,user_2,user_3,user_4,user_5])
session.commit()

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
session.add_all([category_1,category_2,category_3,category_4,category_5,category_6,category_7,category_8,category_9,category_10,category_11])
session.commit()

new_product = Products(name='تیشرت مردانه',color='آبی',quantity=50,user=user_5.user_id,category=category_11.category_id,gender='مردانه',brand='Nike',material='نخی',date=date(2024,7,1),picture=open('C:/Users/maryam/Pictures/Camera Roll/عکس های سایت/تیشرت مردانه.jpg','rb').read(),price=50000)  
session.add_all([new_product])
session.commit()


# class Socks(base) : 
#     __tablename__ = 'socks'

#     sock_id = Column('sock_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     description = Column('description',String)


# class Coats(base) : 
#     __tablename__ = 'coats'

#     coat_id = Column('coat_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     description = Column('description',String)


# class Bags(base) : 
#     __tablename__ = 'bags'

#     bag_id = Column('bag_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     description = Column('description',String)

# class Scarves(base) : 
#     __tablename__ = 'scarves'

#     scarf_id = Column('scarf_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     description = Column('description',String)


# class Shoes(base) : 
#     __tablename__ = 'shoes'

#     shoe_id = Column('shoe_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     description = Column('description',String)

# class Tshirts(base) : 
#     __tablename__ = 'tshirts'

#     tshirt_id = Column('tshirt_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     description = Column('description',String)


# class Skirts(base) : 
#     __tablename__ = 'skirts'

#     skirt_id = Column('skirt_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     description = Column('description',String)


# class Pants(base) : 
#     __tablename__ = 'pants'

#     pant_id = Column('pant_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     description = Column('description',String)

# class Hats(base) : 
#     __tablename__ = 'hats'

#     hat_id = Column('hat_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     description = Column('description',String)


# class Hoodies(base) : 
#     __tablename__ = 'hoodies'

#     hoodie_id = Column('hoodie_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     size = Column('size',String)
#     with_hood = Column('with_hood',Boolean)
#     description = Column('description',String)


# class Belts(base) : 
#     __tablename__ = 'belts'

#     belt_id = Column('belt_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     description = Column('description',String)
 

# class Orders(base) : 
#     __tablename__ = 'orders'

#     order_id = Column('order_id' ,Integer, primary_key=True, autoincrement=True)
#     product_id = Column('product_id',Integer,foreign_key=True)
#     user_id = Column('user_id',Integer,foreign_key=True)
#     order_date= Column('order_date',Date)
#     payment_method = Column('payment_method',String)
#     order_status = Column('order_status',Boolean)
#     quantity = Column('quantity',Integer)
 









# socks_1 = Socks(product_id= , description='راه راه-متوسط') 
# socks_2 = Socks(product_id= , description='ساده-بزرگ')
# socks_3 = Socks(product_id= , description='طرح دار-کوچک')
# socks_4 = Socks(product_id= , description='خال خالی-کوچک')
# socks_5 = Socks(product_id= , description='ساده-متوسط')
# session.add_all([socks_1,socks_2,socks_3,socks_4,socks_5])


# coat_1 = Coats(product_id= , size= , description='') 
# coat_2 = Coats(product_id= , size= ,description='')
# coat_3 = Coats(product_id= , size= ,description='')
# coat_4 = Coats(product_id= , size= ,description='')
# coat_5 = Coats(product_id= , size= ,description='')
# session.add_all([coat_1,coat_2,coat_3,coat_4,coat_5])


# bag_1 = Bags(product_id= , description='') 
# bag_2 = Bags(product_id= , description='')
# bag_3 = Bags(product_id= , description='')
# bag_4 = Bags(product_id= , description='')
# bag_5 = Bags(product_id= , description='')
# session.add_all([bag_1,bag_2,bag_3,bag_4,bag_5])


# scarf_1 = Scarves(product_id= , description='') 
# scarf_2 = Scarves(product_id= , description='')
# scarf_3 = Scarves(product_id= , description='')
# scarf_4 = Scarves(product_id= , description='')
# scarf_5 = Scarves(product_id= , description='')
# session.add_all([scarf_1,scarf_2,scarf_3,scarf_4,scarf_5])


# shoes_1 = Shoes(product_id= ,size='' , description='') 
# shoes_2 = Shoes(product_id= ,size='' , description='')
# shoes_3 = Shoes(product_id= ,size='' , description='')
# shoes_4 = Shoes(product_id= ,size='' , description='')
# shoes_5 = Shoes(product_id= ,size='' , description='')
# session.add_all([shoes_1,shoes_2,shoes_3,shoes_4,shoes_5])


# tshirt_1 = Tshirts(product_id= ,size='' , description='') 
# tshirt_2 = Tshirts(product_id= ,size='' , description='')
# tshirt_3 = Tshirts(product_id= ,size='' , description='')
# tshirt_4 = Tshirts(product_id= ,size='' , description='')
# tshirt_5 = Tshirts(product_id= ,size='' , description='')
# session.add_all([tshirt_1,tshirt_2,tshirt_3,tshirt_4,tshirt_5])


# skirt_1 = Skirts(product_id= ,size='' , description='') 
# skirt_2 = Skirts(product_id= ,size='' , description='')
# skirt_3 = Skirts(product_id= ,size='' , description='')
# skirt_4 = Skirts(product_id= ,size='' , description='')
# skirt_5 = Skirts(product_id= ,size='' , description='')
# session.add_all([skirt_1,skirt_2,skirt_3,skirt_4,skirt_5])


# pant_1 = Pants(product_id= ,size='' , description='') 
# pant_2 = Pants(product_id= ,size='' , description='')
# pant_3 = Pants(product_id= ,size='' , description='')
# pant_4 = Pants(product_id= ,size='' , description='')
# pant_5 = Pants(product_id= ,size='' , description='')
# session.add_all([pant_1,pant_2,pant_3,pant_4,pant_5])


# hat_1 = Hats(product_id= ,description='') 
# hat_2 = Hats(product_id= ,description='')
# hat_3 = Hats(product_id= ,description='')
# hat_4 = Hats(product_id= ,description='')
# hat_5 = Hats(product_id= ,description='')
# session.add_all([hat_1,hat_2,hat_3,hat_4,hat_5])


# hoodie_1 = Hoodies(product_id= ,size='',with_hood=True ,description='') 
# hoodie_2 = Hoodies(product_id= ,size='',with_hood=False , description='')
# hoodie_3 = Hoodies(product_id= ,size='',with_hood=False ,description='')
# hoodie_4 = Hoodies(product_id= ,size='',with_hood=True ,description='')
# hoodie_5 = Hoodies(product_id= ,size='',with_hood=False ,description='')
# session.add_all([hoodie_1,hoodie_2,hoodie_3,hoodie_4,hoodie_5])



# belt_1 = Belts(product_id= ,description='') 
# belt_2 = Belts(product_id= ,description='')
# belt_3 = Belts(product_id= ,description='')
# belt_4 = Belts(product_id= ,description='')
# belt_5 = Belts(product_id= ,description='')
# session.add_all([belt_1,belt_2,belt_3,belt_4,belt_5])

# order_1 = Orders(product_id= ,user_id= ,order_date=date() ,payment_method='' ,order_status=True ,quantity= ) 
# order_2 = Orders(product_id= ,user_id= ,order_date=date() ,payment_method='' ,order_status=False ,quantity= )
# order_3 = Orders(product_id= ,user_id= ,order_date=date() ,payment_method='' ,order_status=False ,quantity= )
# order_4 = Orders(product_id= ,user_id= ,order_date=date() ,payment_method='' ,order_status=True ,quantity= )
# order_5 = Orders(product_id= ,user_id= ,order_date=date() ,payment_method='' ,order_status=True ,quantity= )
# session.add_all([order_1,order_2,order_3,order_4,order_5])


# session.commit()
session.close()

    
