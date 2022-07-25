from email.policy import default
from itertools import product
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    search_tags = models.TextField(blank=True,null=True)
    available = models.BooleanField()
    image = models.ImageField(default='default.jpg',upload_to='product_imgs',null=True,blank=True)

    def __str__(self):
        return f'({self.id}-{self.name})'

class featuredProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

