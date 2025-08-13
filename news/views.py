from django.shortcuts import render, get_object_or_404, redirect
from main.models import Category, News
from main.models import Comment
from main.forms import CommentForm


def home(request):
    news = News.objects.all().order_by('-id')[:5]
    india = News.objects.filter(cate__title="india news")[:5]
    bollywood = News.objects.filter(cate__title="bollywood news")[:5]
    sport = News.objects.filter(cate__title="sports news")[:5]
    online = News.objects.filter(cate__title="Online")[:5]

    context = {
        'news': news,
        'india': india,
        'bollywood': bollywood,
        'sport': sport,
        'online': online,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    data = get_object_or_404(News, pk=id)
    comments = Comment.objects.filter(news=data).order_by('-created_at')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = data
            comment.save()
           

    latest_news = News.objects.all().order_by('-id')[:6]

    return render(request, 'detail.html', {
        'data': data,
        'news': latest_news,
        'comments': comments,
        'form': form,
    })


def india(request):
    data = News.objects.filter(cate__title="india news")
    return render(request, 'india.html', {'data': data})

def bollywood(request):
    data = News.objects.filter(cate__title="bollywood news")
    return render(request, 'bollywood.html', {'data': data})

def sport(request):
    data = News.objects.filter(cate__title="sports news")
    return render(request, 'sport.html', {'data': data})

def online(request):
    data = News.objects.filter(cate__title="Online")
    return render(request, 'online.html', {'data': data})

def search(request):
    query = request.GET.get('q', '')
    data = News.objects.filter(desc__icontains=query) if query else []
    return render(request, 'search.html', {'query': query, 'data': data})
