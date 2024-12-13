import datetime
from django.db import models
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute


class Category(models.Model):
    c_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.c_id} {self.name}'

class User(models.Model):
    u_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nation_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.u_id} {self.first_name} {self.last_name}'

class Product(models.Model):
    GENDER_CHOICES = [
        ('female','زن'),
        ('male','مرد'),
        ('child','کودک'),
        ('sport','اسپرت')
    ]
    p_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    gender = models.CharField(max_length=6 , choices=GENDER_CHOICES, default='sport')
    price = models.DecimalField(default=0,decimal_places=2,max_digits=12)
    picture = models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return f'{self.p_id} {self.p_name}'

class Coat(models.Model):
    c_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.c_id} {self.size}'


class Hat(models.Model):
    h_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.h_id}'


class Bag(models.Model):
    b_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.b_id}'

class Socks(models.Model):
    s_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    design = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.s_id} {self.design}'

class Scarf(models.Model):
    SEASON_CHOICE = [
        ('spring','بهار'),
        ('summar','تابستان'),
        ('autumn','پاییز'),
        ('winter','زمستان')
    ]
    s_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    season = models.CharField(max_length=6,choices=SEASON_CHOICE,default='spring')
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    design = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.s_id} {self.season} {self.design}'

class Shoes(models.Model):
    sh_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.sh_id} {self.size} {self.description}'

class Shirt(models.Model):
    sh_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.sh_id} {self.size}'

class Hoodie(models.Model):
    HAT_CHOICE = [
        ('0','بدون کلاه'),
        ('1','با کلاه')
    ]
    h_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    hat = models.CharField(max_length=1,choices=HAT_CHOICE,default='0')
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.sh_id} {self.size} {self.description}'

class Belt(models.Model):
    b_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)

    def __str__(self):
        return f'{self.b_id} {self.description}'

class Pants(models.Model):
    p_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.p_id} {self.size} {self.description}'

class Skirt(models.Model):
    s_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=500 , default=' ',blank=False,null=False)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.p_id} {self.size} {self.description}'

class Order(models.Model):
    o_id = models.CharField(max_length=10)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=500 , default=' ', blank=False)
    number = models.IntegerField(default=1)

    def __str__(self):
        return