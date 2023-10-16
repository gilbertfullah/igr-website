from django.shortcuts import render, get_object_or_404
from news_and_media.models import Release, News
from django.core.paginator import Paginator
from .forms import CommentCreateForm, ReplyCreateForm
from taggit.models import Tag
from .models import Comment

def releases(request):
    releases = Release.objects.all().order_by('-published_date')
    authors = Release.objects.values_list('author', flat=True).distinct()[:2]
    tags = [tag.name for release in releases for tag in release.tags.all()]
    tags = list(set(tags))  # Deduplicate tag names
    selected_author = request.GET.get('author', 'all')
    selected_tag = request.GET.get('tag', 'all')
    
    paginator = Paginator(releases, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if selected_author != 'all':
        releases = releases.filter(author=selected_author)
    
    if selected_tag != 'all':
        releases = releases.filter(tags__name=selected_tag)
    
    context = {
        'releases': page_obj,
        'authors': authors,
        'tags': tags,
        'selected_author': selected_author,
        'selected_tag': selected_tag,
    }
    
    return render(request, 'release.html', context)

def release_detail(request, release_id):
    release = get_object_or_404(Release, id=release_id)
    tags = release.tags.all()
    
    # Retrieve all comments for the post
    comments = Comment.objects.filter(parent_post=release)
    
    # Retrieve all replies for each comment
    for comment in comments:
        comment.replies = Reply.objects.filter(parent_comment=comment)
    
    context = {
        'release': release,
        'tags': tags,
        'comments': comments,
    }
    
    return render(request, 'release-details.html', context)

def add_comment(request, release_id):
    release = get_object_or_404(Release, id=release_id)

    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_post = release
            comment.save()
    else:
        commentform = CommentForm()

    return render(request, 'release-details.html', {'commentform': commentform, 'release': release})

def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        replyform = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.parent_comment = comment
            reply.save()
    else:
        replyform = ReplyForm()

    return render(request, 'release-details.html', {'replyform': replyform, 'comment': comment})

def releases_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    releases = Release.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'releases': releases,
    }

    return render(request, 'releases_by_tag.html', context)

def news(request):
    news = News.objects.all().order_by('-published_date')
    authors = News.objects.values_list('posted_by', flat=True).distinct()
    tags = [tag.name for n in news for tag in n.tags.all()]
    tags = list(set(tags))  # Deduplicate tag names
    selected_author = request.GET.get('posted_by', 'all')
    selected_tag = request.GET.get('tag', 'all')
    
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if selected_author != 'all':
        news = news.filter(posted_by=selected_author)
    
    if selected_tag != 'all':
        news = news.filter(tags__name=selected_tag)
    
    context = {
        'news': page_obj,
        'authors': authors,
        'tags': tags,
        'selected_author': selected_author,
        'selected_tag': selected_tag,
    }
    
    return render(request, 'in_the_news.html', context)
