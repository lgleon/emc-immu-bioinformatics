from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.testing, name='testing'),
    path('job_status/', views.job_status, name='job_status'),
]

