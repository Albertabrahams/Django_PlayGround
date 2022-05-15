from django.contrib import admin

from .models import Customer, Type

admin.site.register(Type)
admin.site.register(Customer)