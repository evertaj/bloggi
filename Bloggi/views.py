from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from Bloggi.forms import CommentForm
from Bloggi.models import Article, Comment

def Home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')

def show_article(request, article_id):
    form = CommentForm()
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.all()
    return render(request, 'article.html', {'article': article, 'comments':comments, 'form':form})

def create_comment(request, article_id):
    comment = Comment()
    comment.text = request.POST.get("text", '')
    if request.user.is_authenticated():
        comment.user_id = request.user.id
    comment.article_id = article_id
    comment.save()
    return redirect('article', article_id)


