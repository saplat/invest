from django.urls import path

from . import consumers

ws_urlpatterns = [
    path('ws/graph', consumers.GraphConsumer.as_asgi())
]