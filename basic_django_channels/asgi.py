"""
ASGI config for basic_django_channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from integers.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django_channels.settings')

application=ProtocolTypeRouter({
	'http':get_asgi_application(),
	'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns)) # se le agregara la especie de url proveniente de routing.py
})


