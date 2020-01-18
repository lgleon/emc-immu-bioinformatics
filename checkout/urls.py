from django.urls import path
from .views import checkout, index

urlpatterns = [
    path('', index, name='index'),
    path('', checkout, name='checkout'),
]