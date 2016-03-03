from django.shortcuts import render
from django.shortcuts import render_to_response

from Bloggi.models import Article, Comment
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
    comments = Comment.objects.all()
    return render(request, 'article.html', {'article': article, 'comments':comments})
