from django import forms
from django.forms import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class new_Product(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
class Register(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username','email','password1','password2']

class Login(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username','email','password1']

