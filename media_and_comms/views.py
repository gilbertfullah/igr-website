from django.shortcuts import render
from news_and_media.models import Release, News
from django.core.paginator import Paginator
from news_and_media.forms import CommentCreateForm, ReplyCreateForm

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
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()
    
    context = {
        'release': release,
    }
    
    return render(request, 'release_detail.html', context)

def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)
    replyform = ReplyCreateForm()
    
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post            
            comment.save()
            
    context = {
        'post' : post,
        'comment': comment,
        'replyform': replyform
    }

    return render(request, 'snippets/add_comment.html', context)

def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform = ReplyCreateForm()
    
    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment            
            reply.save()
            
    context = {
        'reply' : reply,
        'comment': comment,
        'replyform': replyform
    }

    return render(request, 'snippets/add_reply.html', context)

def comment_delete_view(request, pk):
    post = get_object_or_404(Comment, id=pk, author=request.user)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('post', post.parent_post.id )
        
    return render(request, 'a_posts/comment_delete.html', {'comment' : post})

def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    
    if request.method == "POST":
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('post', reply.parent_comment.parent_post.id )
        
    return render(request, 'a_posts/reply_delete.html', {'reply' : reply})



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
