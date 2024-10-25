"""
ASGI config for realtime project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from utils.routing import ws_urlpatterns
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP requests still handled by Django
    "websocket": AuthMiddlewareStack(  # WebSocket connections go through AuthMiddlewareStack
        URLRouter(
            ws_urlpatterns  # Your WebSocket routing
        )
    ),
})
