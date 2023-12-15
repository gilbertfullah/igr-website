from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.focus_areas, name='focus_areas'),
]