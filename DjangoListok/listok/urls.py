from django.urls import path
from . import views


urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('add_client/', views.add_client, name='add_client')
]