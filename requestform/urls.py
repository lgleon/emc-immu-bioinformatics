from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.testing, name='testing'),
    path('job_request/', views.job_request, name='job_request'),
    path('general_info/', views.general_info, name='general_info'),
    path('analysis_type/', views.analysis_type, name='analysis_type'),
]