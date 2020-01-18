from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients_data/', views.clients_data, name='clients_data'),
]