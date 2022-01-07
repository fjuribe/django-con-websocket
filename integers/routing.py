from django.urls import path
from django.conf.urls import url
# from .consumers import *

from . import consumers

ws_urlpatterns = [
    path('ws/some_url/', consumers.WSConsumer.as_asgi()),
    path('ws/probando/', consumers.Probando.as_asgi()),
    path('ws/respuesta/',consumers.RespuestaModelo.as_asgi()),
    path('ws/asincrono/',consumers.WSConsumerAsync.as_asgi()),
    path('ws/estoesunaprueba/<int:pk>/<int:id2>/',consumers.Probando2.as_asgi()),

]