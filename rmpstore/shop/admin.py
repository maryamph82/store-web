from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["phone_number", "first_name", "last_name", "national_code","postal_code","address","birth_date",]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups"]
    filter_horizontal = ["groups", "user_permissions"]
    ordering = ["username"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(models.Categorie)
admin.site.register(models.Product)
admin.site.register(models.Coat)
admin.site.register(models.Hat)
admin.site.register(models.Hoodie)
admin.site.register(models.Tshirt)
admin.site.register(models.Shoe)
admin.site.register(models.Skirt)
admin.site.register(models.Sock)
admin.site.register(models.Scarve)
admin.site.register(models.Pant)
admin.site.register(models.Bag)
admin.site.register(models.Belt)
admin.site.register(models.Order)


