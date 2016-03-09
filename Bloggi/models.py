from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT_LEN = 600

class Article(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self

    def comments_count(self):
        p = Comment.objects.all().filter(article_id = self.id)
        return len(p)

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    text = models.TextField(blank=True)
    article = models.ForeignKey(Article, null=True, blank=True)
    approved = models.NullBooleanField()

    def __str__(self):
        return self.text
