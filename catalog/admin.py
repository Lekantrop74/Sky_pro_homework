from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Category, Product, Contact, BlogPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(BlogPost)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["title"]
