from django.urls import path
from .consumers import IndicatorConsumer

websocket_urlpatterns = [
    path('ws/indicators/', IndicatorConsumer.as_asgi()),
]
