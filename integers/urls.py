from django.urls import path
from .views import index
from integers.views import *

urlpatterns = [
    path('', index),
    path('prueba/',Prueba.as_view())

]
