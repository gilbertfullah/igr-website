from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('who-we-are/', include('who_we_are.urls')),
    path('focus-areas/', include('focus_areas.urls')),
    path('contact-us/', include('contact_us.urls')),
    path('faqs/', include('faqs.urls')),
    path('media-and-communication/', include('media_and_comms.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
