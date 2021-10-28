from django.urls import path
from django.conf.urls import url
from .consumers import *

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi()),
    path('ws/probando/', Probando.as_asgi()),
    path('ws/estoesunaprueba/<int:id>/<int:id2>/',Probando2.as_asgi()),
]
