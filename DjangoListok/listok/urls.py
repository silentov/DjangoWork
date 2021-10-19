from django.urls import path
from . import views


urlpatterns = [
    path('', views.clients, name='clients'),
    path('', views.add_client, name='add_client')
]