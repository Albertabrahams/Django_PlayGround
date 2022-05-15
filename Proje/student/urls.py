from django.urls import path
from .views import home,henry,kral

urlpatterns = [
    path('', home, name='home'),
    path('henry/', henry, name='henry'),
    path('kral/', kral, name='kral')
]