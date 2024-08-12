from django.shortcuts import render
from .models import Blog
from interview.models import Interview
from poem.models import Poem
from article.models import Article

def index(request):
    # datas for featured
    featured_interviews = Interview.objects.all().order_by('-created_at')[:1]
    featured_poems = Poem.objects.all().order_by('-created_at')[:1]
    featured_articles = Article.objects.all().order_by('-created_at')[:1]
    
    # datas for blog
    interviews = Interview.objects.all().order_by('-created_at')[:3]
    poems = Poem.objects.all().order_by('-created_at')[:3]
    articles = Article.objects.all().order_by('-created_at')[:3]
    
    featured_blogs = Blog.objects.all().order_by('-created_at')[:3]

    context = {
        'featured_interviews': featured_interviews,
        'featured_poems': featured_poems,
        'featured_articles': featured_articles,
        'interviews': interviews,
        'poems': poems,
        'articles': articles,
        'featured_blogs': featured_blogs,  # Add this line to pass featured blogs to context
    }
    return render(request, 'index.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog_detail.html', context)

def about(request):
    return render(request, 'aboutus.html')
