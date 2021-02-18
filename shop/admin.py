from shop.views import AddProduct
from django.contrib import admin
from .models import *
# Register your models here.
# user: eshop pass: 1q2w3e

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Order)