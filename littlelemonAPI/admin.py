from django.contrib import admin
from .models import Category, MenuItem, Rating

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Rating)