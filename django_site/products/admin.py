from django.contrib import admin
from .models import Product
admin.site.register(Product)
from .models import Category
admin.site.register(Category)