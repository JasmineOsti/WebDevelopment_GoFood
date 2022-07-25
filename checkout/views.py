from ast import Continue
import json
from multiprocessing import context
from tokenize import Token
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.models import User_Address
from cart.models import Delivery, Order
from checkout.models import ShippingAddress
from django.contrib.auth.decorators import login_required

import datetime

from django.contrib import messages
from myorder.models import MyOrder
from myorder.views import myOrder

# Create your views here. 
@login_required
def checkout(request):
    customer = request.user

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    addressExists = False
    if (User_Address.objects.filter(user_info = customer.id).exists()):
        addressData = User_Address.objects.filter(user_info = customer.id)[0]
        addressExists=True
    else:
        addressData=[]
        addressExists=False

    context={
        'items':items,
        'order':order,
        'customer':customer,
        'addressExists':addressExists,
        'addressData':addressData,
        
    }
    return render(request,'checkout.html',context)

def paymentSuccess(request,orderID,pm):

    getOrder = Order.objects.get(id = orderID)
    context={
        'getOrder':getOrder,
        'pm':pm,
    }
    return render(request,'PaymentSuccess.html',context)\

def getDeliveryDate(days):
    newDate = datetime.date.today() + datetime.timedelta(days=days)
    return newDate


def saveShippingData(request):
    if request.method == "GET":

        print("DATA RECEIVED")
        o_id = request.GET.get('order')
        phone = request.GET.get('phone')
        email = request.GET.get('email')
        city = request.GET.get('city')
        address =request.GET.get('address')
        street = request.GET.get('street')
        postalcode = request.GET.get('postalcode')
        description =request.GET.get('description')
        pm = request.GET.get('pm')
        customer = request.user
        current_date = datetime.date.today()  
        orderid = Order.objects.get(user_info = customer, complete=False)

        getOrder = Order.objects.get(id = o_id)

        items = getOrder.orderitem_set.all()

    dataSaved=""

    if pm == "COD":    
        getOrder.complete = True
        getOrder.payment_method = "Cash on Delivery"
        getOrder.save()

        saveData = ShippingAddress(user_info=customer,orderid=orderid, phone=phone, email=email, city=city,address=address,street=street,postalcode=postalcode,description=description)
        saveData.save()

        saveDelivery=Delivery(o_id = getOrder,deliveryDate=getDeliveryDate(2))
        saveDelivery.save()

        delv = Delivery.objects.get(o_id=getOrder)
        adrs = ShippingAddress.objects.get(orderid=getOrder)

        savemyOrder=MyOrder(user_info=customer,o_id = getOrder,delivery=delv,address=adrs)
        savemyOrder.save()

        dataSaved = "Saved PM: COD"    

    return JsonResponse(dataSaved, safe=False)
