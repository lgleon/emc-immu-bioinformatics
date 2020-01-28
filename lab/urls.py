from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_updated/', views.job_updated, name='job_updated'),
    #path('projects/', views.projects, name='projects'),
    path('project1/', views.project1, name='project1'),
    path('project2/', views.project2, name='project2'),
    path('project3/', views.project3, name='project3'),
    path('project4/', views.project4, name='project4'),
    path('work/', views.work, name='work'),
    path('team/', views.team, name='team'),
    #path('', views.testing, name='testing'),
    path('job_status/', views.job_status, name='job_status'),
]

