from django.contrib import admin
from .models import Category, MenuItem, Rating

# Register your models here.
# admin.site.register(MenuItem)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'price', 'inventory', 'category'
    )
admin.site.register(Category)
admin.site.register(Rating)