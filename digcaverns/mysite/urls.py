from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('resume', views.resume, name='resume'),
    path('display_resume', views.display_resume, name='display_resume')
]
