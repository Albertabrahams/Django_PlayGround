from django.urls import path
from .views import home,henry,kral,student_num

urlpatterns = [
    path('', home, name='home'),
    path('henry/', henry, name='henry'),
    path('kral/', kral, name='kral'),
    path('num/', student_num, name='student_num'),
]