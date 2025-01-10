from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import CreateAcc

def main_page(request):
    return render(request,'homepage.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect('home')
    else:
        messages.success(request, ("مشکلی در ورود شما وجود دارد"))
        return render(request , 'login.html')

def create_acc(request):
    form = CreateAcc()
    if request.method == "POST":
        form = CreateAcc(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request , username = username , password = password)
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

def product_page(request):
    return render(request , 'product.html')

def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")
