from django.conf.urls import url
import Bloggi.views

urlpatterns = [
    url(r'^about/$', Bloggi.views.About, name='About'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', Bloggi.views.show_article, name='Article'),
    url(r'^articles/(?P<article_id>[0-9]+)/comments/$', Bloggi.views.create_comment, name='create_comment'),
    url(r'^home/create_article/$', Bloggi.views.create_article, name='create_article'),
    url(r'^home/$', Bloggi.views.Home, name='Home'),
    url(r'^$', Bloggi.views.Home, name='Home')
]
