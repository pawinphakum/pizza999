from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Favorite)
admin.site.register(Pizza)
admin.site.register(Topping)
