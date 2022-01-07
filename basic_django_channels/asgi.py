"""
ASGI config for basic_django_channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django_channels.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.http import AsgiHandler
from integers.routing import ws_urlpatterns


application=ProtocolTypeRouter({
	'http':AsgiHandler(),
	'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns)) # se le agregara la especie de url proveniente de routing.py
})


