from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    text = models.CharField(max_length=50)
    def __str__(self) :
        return self.text

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE) # this is not saved as name of categorys but as the id of taht category
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='product_pics/')
    def __str__(self) :
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete= models.CASCADE)
    customer = models.ForeignKey(User, on_delete= models.CASCADE) # this is not saved as name of categorys but as the id of that category
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(max_length=100000000)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField(default= datetime.datetime.today)
    
