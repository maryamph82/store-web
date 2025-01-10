from venv import create

from django.urls import path,include
from .views import main_page , login_user,create_acc,kid_page,contact_page,man_page,woman_page,product_page, logout_user

urlpatterns = [
    path('', main_page,name = "home"),
    path('login.html/',login_user,name = "login"),
    path('createAccount.html/',create_acc,name = "createAccount"),
    path('kids.html/', kid_page, name="kids"),
    path('contact.html/', contact_page , name="contact"),
    path('manpage.html/', man_page, name="men"),
    path('womanpage.html/', woman_page, name="women"),
    path('product.html/', product_page, name="product"),
    path('logout/', logout_user, name="logout")

]