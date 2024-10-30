from django.contrib import admin
from .models import Product, Category, Menu


admin.site.register([Category, Menu, Product])