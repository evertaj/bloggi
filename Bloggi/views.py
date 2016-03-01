from django.shortcuts import render
from Bloggi.models import Article
from django.shortcuts import get_object_or_404

def Home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'article': article})
