from django.urls import path

from . import views

urlpatterns = [
    path('', views.me, name='me'),
    path('me', views.me, name='me'),
    path('resume', views.resume, name='resume'),
    path('blog', views.resume, name='blog')
]
