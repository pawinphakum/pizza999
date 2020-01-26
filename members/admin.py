from django.contrib import admin
from .models import *

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    ordering = ['-name']
    search_fields = ['name']

# Register your models here.
admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Topping)
