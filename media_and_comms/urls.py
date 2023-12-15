from django.urls import path
from . import views

urlpatterns = [
    path('releases/', views.releases, name='releases'),
    path('release/<int:release_id>/', views.release_detail, name='release_detail'),
    
    path('tag/<slug:tag_slug>/', views.releases_by_tag, name='releases_by_tag'),
    
    path('release/<int:post_id>/add-comment/', views.add_comment, name='add_comment'),
    path('release/<int:post_id>/add-reply/', views.add_reply, name='add_reply'),
    
    path('igr-in-the-news/', views.news, name='in_the_news'),
]