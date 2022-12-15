from django.urls import path
from . import views


urlpatterns = [
    path('geomap', views.IpadGeoMapView),
    path('worldline', views.WorldLineChartView),
]