from django.shortcuts import render,redirect
from django.http import request
from .forms import *
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def AddProduct(request): # for admin
    if request.method == 'POST':
        form = new_Product(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = new_Product()
    context = {'form': form}
    return render(request,'shop/addproduct.html',context)

def index(request):
    
    if request.method == 'POST':
        remove = request.POST.get('remove')
        product = request.POST.get('prod')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if cart[product] <=1:
                        cart.pop(product)
                    else:
                        cart[product]= quantity-1
                else:
                    cart[product]= quantity+1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product]= 1
        request.session['cart']= cart
        
        return redirect('/')
    
    else:
        
        pro = Products.objects.all()
        cat = Category.objects.all()
        return render(request,'shop/index.html',{'pro':pro,'cat':cat})

def Registration(request):
    form = Register()
    if request.method =='POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    return render(request,'shop/register.html',{'form':form})
        

def filtered_page(request,pk):
    if request.method == 'POST':
        p_id = request.POST.get('prod')
       
        return redirect('/')
    else:
        cat = Category.objects.all()
        items = Products.objects.filter(category = pk)
        return render(request,'shop/filtered.html',{'items':items,'cat':cat})

def logoutp(request):
    logout(request)
    return redirect('/')

@login_required
def cart(request):
    ids = list()
    for i in request.session.get('cart').keys():
        if i !='null':
            ids.append(i)
    pros = Products.objects.filter(id__in = ids)
    return render(request,'shop/cart.html',{'pros': pros})

@login_required
def checkout(request):
    print('hello')
    if request.method == 'POST':
        ids = list()
        
        for i in request.session.get('cart').keys():    
            if i !='null':                
                ids.append(i)
                
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        customer = request.user
        
        products = Products.objects.filter(id__in = ids)
        
        for p in products:
            order = Order(product=p,customer=customer,quantity=cart.get(str(p.id)),price=p.price,phone=phone,address=address)
        order.save()
        request.session['cart'] = {}

    return redirect('/')