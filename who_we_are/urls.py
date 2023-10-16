from django.urls import path, include
from . import views

urlpatterns=[
    #path('', views.who_we_are, name='who_we_are'),
    path('', views.about, name='about_us'),
]