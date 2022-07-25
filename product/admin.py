from django.contrib import admin
from product.models import Products,featuredProduct
# Register your models here.
admin.site.register(Products)
admin.site.register(featuredProduct)
