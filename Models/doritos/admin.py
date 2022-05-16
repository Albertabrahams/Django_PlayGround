from django.contrib import admin

from .models import Customer, Customer2, Type

admin.site.register(Type)
admin.site.register(Customer)
admin.site.register(Customer2)