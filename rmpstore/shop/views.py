from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import CustomUserCreationForm
from .models import Product


def main_page(request):
    all_product = Product.objects.all()
    return render(request,'homepage.html',{'products':all_product})

def login_user(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect('home')
    else:
        messages.success(request, ("مشکلی در ورود شما وجود دارد"))
        return render(request , 'login.html')

def create_acc(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request , phone_number = phone_number , password = password)
            login(request,user)
            messages.success(request, ("اکانت شما با موفقیت ساخته شد"))
            return redirect("home")
        else:
            messages.success(request, ("مشکلی در ثبت نام شما وجود دارد"))
            return redirect("createAccount")
    else:
        return render(request , 'createAccount.html',{'form':form})

def contact_page(request):
    return render(request , 'contact.html')

def kid_page(request):
    return render(request , 'kids.html')

def man_page(request):
    return render(request , 'manpage.html')

def woman_page(request):
    return render(request , 'womanpage.html')

def product_page(request,pk):
    product = Product.objects.get(id=pk)
    return render(request , 'product.html' , {'product':product})

def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")
