from django.urls import path
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]