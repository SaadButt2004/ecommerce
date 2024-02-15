from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(Category)

# class ProductImageAdmin(admin.StackedInline):
#     model = ProductImage 

# class ProductAdmin(admin.StackedInline):
#     inlines = [ProductImageAdmin]

admin.site.register(Product)

admin.site.register(ProductImage)