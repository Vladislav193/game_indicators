from django.urls import path
form .consumers import IndicatorConsumer

websocket_urlpatterns = [
    path('ws/indicators/', IndicatorConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]