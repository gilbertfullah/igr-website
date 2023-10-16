from django.urls import path
from . import views

urlpatterns = [
    path('releases/', views.releases, name='releases'),
    path('release/<int:release_id>/', views.release_detail, name='release_detail'),
    
    path('igr-in-the-news/', views.news, name='in_the_news'),
]