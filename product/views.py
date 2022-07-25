from django.urls import reverse
from itertools import product
import json
from multiprocessing import context
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from cart.models import Order

from product.models import Products
from django.contrib.auth.decorators import login_required

# Create your views here.
def searchResult(request):
    allproducts = Products.objects.all()
    current_user = request.user

    item_name = request.GET.get('item_name')
    if item_name!= "" and item_name is not None:
        allproducts = allproducts.filter(search_tags__icontains=item_name)
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    context={
        'allproducts':allproducts,
        'item_name':item_name,
        'current_user':current_user,
        'order':order,

    }
    return render(request,'searchResult.html',context)

def display(request):
    current_user = request.user
   
    filteredProd = Products.objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    context = {
        'filteredProd':filteredProd,
        'order':order,
    }     
    return render (request, 'display.html',context)

def detail(request,item_id):
    allProducts = get_object_or_404(Products, pk=item_id)
    current_user = request.user

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    context={
        'allProducts':allProducts,
        'order':order,
    }
    return render(request,'productDetail.html',context)


