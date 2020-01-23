from django.contrib import admin
from .models import Article, Meta, Categorie

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    
    admin.site.register(Product, ProductAdmin)
    admin.site.register(ProductItem)