from .views import LocationConsumer
from django.urls import path,include

ws_urlpatterns = [
    path('ws/livelocation/',LocationConsumer.as_asgi())
]