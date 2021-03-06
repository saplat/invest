from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('FB', views.FB),
    path('GOOG', views.GOOG),
    path('AMZN', views.AMZN),
    path('AAPL', views.AAPL),
    path('', views.layout),
    path('', views.index),
    path('news', views.news, name='news'),
    path('stocktracker', views.stockTracker, name='Тут пока все активы'),
    path('stockpicker', views.stockPicker, name = 'stockpicker')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
