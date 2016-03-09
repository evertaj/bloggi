from django.conf.urls import url

urlpatterns = [
    url(r'^about/$', 'Bloggi.views.About', name='About'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'Bloggi.views.show_article', name='article'),
    url(r'^articles/(?P<article_id>[0-9]+)/comments/$', 'Bloggi.views.create_comment', name='create_comment'),
    url(r'^home/$', 'Bloggi.views.Home', name='Home'),
    url(r'^$', 'Bloggi.views.Home', name='Home')
]
