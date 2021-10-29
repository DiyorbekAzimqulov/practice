from django.contrib import admin
from .models import Product, Order, User, Follow
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Follow)
