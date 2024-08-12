from django.shortcuts import render
from .models import Article

# Create your views here.
def article(request): 
    articles = Article.objects.all()
    context  = {
        'articles': articles,
    }
    return render(request, 'article.html', context)

def article_detail(request, pk):
    article_det = Article.objects.get(pk=pk)
    context = {
        'article_det': article_det,
    }
    return render(request, 'article_det.html', context)
    