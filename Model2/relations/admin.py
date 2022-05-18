from django.contrib import admin

from .models import Creator, Language, Framework, Developers

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Developers)