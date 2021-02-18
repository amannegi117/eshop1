from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import TemplateView
from .views import *
urlpatterns = [
path('',index,name='index'),
path('register/',Registration,name='register'),
path('filtered/<int:pk>/',filtered_page,name='filtered'),
path('login/',LoginView.as_view(template_name='shop/login.html'),name='login'),
path('logout/',logoutp,name='logout'),
path('cart/',cart,name='cart'),
path('checkout/',checkout,name='checkout'),
path('shop/cart/checkout',checkout,name='checkout')
]
