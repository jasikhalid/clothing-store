from django.contrib import admin
from razorpay.resources import order

from .models import *
# Register your models here.
admin.site.register(register)
admin.site.register(login)
admin.site.register(products)
admin.site.register(ContactMessage)
admin.site.register(favorites)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(orderitem)