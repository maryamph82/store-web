from django.contrib.auth.forms import UserCreationForm,UserChangeForm,User
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
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
    phone_number = forms.CharField(
        label="",
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
    )
    # email = forms.EmailField(
    #     label="",
    #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    # )
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
    national_code = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'national code'}),
    )

    class Meta:
        model = CustomUser
        fields = ("phone_number", "first_name", "last_name", "national_code","postal_code","address", "password1","password2","birth_date")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("phone_number", "first_name", "last_name", "national_code","postal_code","address","birth_date")
