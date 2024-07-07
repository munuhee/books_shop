from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'author', 'digital')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
