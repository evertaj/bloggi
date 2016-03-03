from django.conf.urls import url, include

urlpatterns = [
    url(r'^about/$', 'Bloggi.views.About', name='About'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'Bloggi.views.show_article', name='article'),
    url(r'^home/$', 'Bloggi.views.Home', name='Home'),
    url(r'^$', 'Bloggi.views.Home', name='Home')
]
