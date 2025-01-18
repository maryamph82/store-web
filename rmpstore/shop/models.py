# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    postal_code = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    national_code = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True,unique=True)
    user_type = models.TextField(blank=True, null=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = [ "first_name", "last_name", "national_code","postal_code","address","birth_date"]

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = 'users'

class Categorie(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'categories'


class Product(models.Model):
    GENDER_CHOICES = [
        ('female', 'female'),
        ('male', 'male'),
        ('child','child'),
        ('sport','sport')
    ]

    product_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categorie, models.DO_NOTHING, blank=True, null=True)
    gender = models.TextField(max_length=6 , choices=GENDER_CHOICES, default='sport',blank=True, null=True)  # This field type is a guess.
    brand = models.TextField(blank=True, null=True)
    material = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    picture = models.ImageField(upload_to='upload/product/')

    class Meta:
        managed = False
        db_table = 'products'

class Bag(models.Model):
    bag_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bags'


class Belt(models.Model):
    belt_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'belts'


class Coat(models.Model):
    coat_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coats'


class Hat(models.Model):
    hat_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hats'


class Hoodie(models.Model):
    hoodie_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    with_hood = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoodies'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CustomUser, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    payment_method = models.TextField(blank=True, null=True)
    order_status = models.BooleanField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Pant(models.Model):
    pant_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pants'


class Scarve(models.Model):
    scarf_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scarves'


class Shoe(models.Model):
    shoe_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoes'


class Skirt(models.Model):
    skirt_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skirts'


class Sock(models.Model):
    sock_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socks'


class Tshirt(models.Model):
    tshirt_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tshirts'

