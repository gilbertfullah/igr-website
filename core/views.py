from django.shortcuts import render, get_object_or_404
from media_and_comms.models import News, Release, Podcast, Gallery

def index(request):
    releases = Release.objects.all().order_by('-published_date')[:3]
    news = News.objects.all().order_by('-published_date')[:3]
    podcasts = Podcast.objects.all().order_by('-published_date')[:3]
    gallery = Gallery.objects.all()[:6]
    
    context = {
        'releases': releases, 
        'news': news,
        'podcasts': podcasts,
        'gallery': gallery,
    }
    
    return render(request, 'index.html', context)

