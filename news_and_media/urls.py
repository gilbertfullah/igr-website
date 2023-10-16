from django.urls import path, include
from news_and_media.views import communication, news_detail, event_detail, release_detail, add_comment

urlpatterns=[
    path('', communication, name='communication'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('news/<int:news_id>/add_comment/', add_comment, name='add_news_comment'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('events/<int:events_id>/add_comment/', add_comment, name='add_events_comment'),
    path('release/<int:release_id>/', release_detail, name='release_detail'),
    path('release/<int:release_id>/add_comment/', add_comment, name='add_comment'),
]