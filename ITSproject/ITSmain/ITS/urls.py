
from django.contrib import admin
from django.urls import path, include
from requests import request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geomap/',include('main.urls')),
    path('auth/',include('authentication.urls')),
    path('table/',include('table.urls')),
]
