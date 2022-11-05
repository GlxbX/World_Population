from django.urls import path
from requests import request

from table import views


urlpatterns = [
    path('t/<int:id>', views.TableView),
]