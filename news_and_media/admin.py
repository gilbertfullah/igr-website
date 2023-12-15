from django.contrib import admin
from django.utils.html import mark_safe
from .models import News, Events, Release, Comment, Gallery, Podcast

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'posted_by', 'published_date']
    list_display = ['title', 'posted_by', 'published_date']
    search_fields = ['title', 'posted_by']
    list_per_page = 10
    
class EventsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'posted_by', 'published_date']
    list_display = ['title', 'posted_by', 'published_date']
    search_fields = ['title', 'posted_by']
    list_per_page = 10

class ReleasesAdmin(admin.ModelAdmin):
    list_filter = ['title', 'author', 'published_date']
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title', 'author']
    list_per_page = 10
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body']
    list_per_page = 10
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10
    
    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="60" height="60" />')
    image_preview.short_description = 'Image Preview'
    
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10


admin.site.register(News, NewsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Release, ReleasesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Podcast, PodcastAdmin)

