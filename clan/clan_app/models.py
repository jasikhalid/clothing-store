from optparse import Option

from django.db import models
from datetime import datetime

# Create your models here.
class register(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postc = models.CharField(max_length=15)
    def __str__(self):
        return self.full_name
class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username
class products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity1 = models.IntegerField()
    quantity2 = models.IntegerField()
    quantity3 = models.IntegerField()
    description = models.TextField(max_length=500)
    ids=models.CharField(max_length=10,unique=True)
    img = models.FileField()
    gender=models.CharField(max_length=10)
    category=models.CharField(max_length=15)
    size=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class favorites(models.Model):
    username = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    product_image = models.FileField()
    price = models.IntegerField()
    def __str__(self):
        return self.product_name
class cart(models.Model):
    ids=models.CharField(max_length=10,unique=True)
    product_name = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField(default=1)
    product_image = models.FileField()
    price = models.IntegerField()
    username = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
