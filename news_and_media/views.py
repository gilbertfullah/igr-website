from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import News, Events, Release, Comment, Podcast, Gallery
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

def communication(request):
    releases = Release.objects.filter(Q(tag='Press Release') | Q(tag='SierraPoll')).order_by('-published_date')
    news = News.objects.all().order_by('-published_date')
    events = Events.objects.all().order_by('-published_date')
    #podcasts = Podcast.objects.all().order_by('-published_date')
    
    paginator = Paginator(releases, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'communication.html', {'news': news, 'events': events, 'releases': page_obj})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

def event_detail(request, event_id):
    event = get_object_or_404(Events, id=news_id)
    return render(request, 'event_detail.html', {'event': event})

def releases(request):
    releases = Release.objects.all().order_by('-published_date')
    return render(request, 'releases.html', {'releases': releases})

def release_detail(request, release_id):
    release = get_object_or_404(Release, id=release_id)
    return render(request, 'release_detail.html', {'release': release})

def comments(request):
    comments = Comment.objects.all().order_by('-published_date')
    return render(request, 'releases.html', {'comments': comments})

def add_comment(request, release_id):
    release = get_object_or_404(Release, id=release_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.POST.get('author')
        comment = Comment.objects.create(release=release, text=text, author=author)
        # You can add any additional logic here, such as validation or notifications
        return redirect('release_detail', release_id=release.id)

    return redirect('release_detail', release_id=release.id)


def in_the_news(request):
    news = News.objects.all()
    
    context = {
        'news': news,
    }
    
    return render(request, 'in_the_news.html', context)