import datetime
from django.db import models
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.category_id} {self.name}'

class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nation_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user_id} {self.first_name} {self.last_name}'

class Product(models.Model):
    GENDER_CHOICES = [
        ('female','زن'),
        ('male','مرد'),
        ('child','کودک'),
        ('sport','اسپرت')
    ]
    product_id = models.IntegerField()
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    gender = models.CharField(max_length=6 , choices=GENDER_CHOICES, default='sport')
    price = models.DecimalField(default=0,decimal_places=2,max_digits=12)
    picture = models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return f'{self.product_id} {self.name}'

class Coat(models.Model):
    SIZES = [
        ('m',38),
        ('l',40),
        ('xl',42)
    ]
    coat_id = models.IntegerField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=3,choices=SIZES,default='m')

    def __str__(self):
        return f'{self.coat_id} {self.size}'


class Hat(models.Model):
    hat_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.hat_id}'


class Bag(models.Model):
    bag_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.bag_id}'

class Socks(models.Model):
    socks_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.socks_id}'

class Scarves(models.Model):
    SEASON_CHOICE = [
        ('spring','بهار'),
        ('summer','تابستان'),
        ('autumn','پاییز'),
        ('winter','زمستان')
    ]
    scarf_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    season = models.CharField(max_length=6,choices=SEASON_CHOICE,default='spring')
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    design = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.scarf_id} {self.season} {self.design}'

class Shoes(models.Model):
    SIZES = [
        ('قالب خیلی کوچک',38),
        ('قالب کوچک',39),
        ('قالب متوسط',40),
        ('قالب بزرگ',41),
        ('قالب خیلی بزرگ',42)
    ]
    shoe_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=15,choices=SIZES,default=1)

    def __str__(self):
        return f'{self.shoe_id} {self.size} {self.description}'

class Shirt(models.Model):
    SIZES = [
        ('m',38),
        ('l',40),
        ('xl',42)
    ]
    shirt_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=3,choices=SIZES,default=1)

    def __str__(self):
        return f'{self.shirt_id} {self.size}'

class Hoodie(models.Model):
    HAT_CHOICE = [
        ('0','بدون کلاه'),
        ('1','با کلاه')
    ]
    SIZES = [
        ('m',38),
        ('l',40),
        ('xl',42)
    ]
    hoodie_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    hat = models.CharField(max_length=1,choices=HAT_CHOICE,default='0')
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=3,choices=SIZES,default=1)

    def __str__(self):
        return f'{self.hoodie_id} {self.size} {self.description}'

class Belt(models.Model):
    belt_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.belt_id} {self.description}'

class Pants(models.Model):
    SIZES = [
        ('m',38),
        ('l',40),
        ('xl',42)
    ]
    pant_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=3,choices=SIZES,default=1)

    def __str__(self):
        return f'{self.pant_id} {self.size} {self.description}'

class Skirt(models.Model):
    SIZES = [
        ('m',42),
        ('l',44),
        ('xl',46)
    ]
    skirt_id = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=3,choices=SIZES,default=1)

    def __str__(self):
        return f'{self.skirt_id} {self.size} {self.description}'

class Order(models.Model):
    o_id = models.IntegerField()
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=500 , default=' ', blank=False)
    number = models.IntegerField(default=1)

    def __str__(self):
        return