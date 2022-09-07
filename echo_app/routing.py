from django.urls import path
from echo_app import consumers

websocket_urlpatterns = [
    path('', consumers.EchoConsumer),
]