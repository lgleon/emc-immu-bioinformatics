from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_submited/', views.job_submited, name='job_submited'),
    path('job_submited/<int:job_id>', views.job_submited, name='job_submited'),
    path('job_submited/<int:priority_status>', views.job_submited, name='job_submited'),
    #path('', views.testing, name='testing'),
    path('job_request/', views.job_request, name='job_request'),
]