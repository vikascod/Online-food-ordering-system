from django.contrib import admin
from core.models import Category, Food
# Register your models here.
# @admin.register(Food)
# class FoodAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'category', 'price', 'desc', 'image']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'category']

admin.site.register(Food)
admin.site.register(Category)