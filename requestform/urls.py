from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.testing, name='testing'),
    path('job_request/', views.job_request, name='job_request'),
]