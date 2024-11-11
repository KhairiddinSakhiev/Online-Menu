from django.contrib import admin
from .models import Product, Category, Menu


admin.site.register([Category, Menu])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'rating', 'category')