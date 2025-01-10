from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateAcc(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control','name':'password','type':'password', 'placeholder': 'password(more than 8 char)'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password',
                                          'placeholder': 'password(confirm)'}),
    )
    phone = forms.CharField(
        label="",
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    )
    postal_code = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'postal code'}),
    )
    address = forms.CharField(
        label="",
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
    )
    birth_day = forms.DateField(
    label="",
    widget=forms.DateInput(attrs={'type': 'date'}),
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1','password2','email','birth_day','postal_code','address','phone')
