from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT_LEN = 700


class Article(models.Model):
    title = models.CharField(max_length = 200, blank=True)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    approved = models.NullBooleanField()

    def __str__(self):
        return self.title

    def get_short(self):
        if len(self.text) > SHORT_TEXT_LEN:
            if self.text[SHORT_TEXT_LEN] == ' ':
                return self.text[:SHORT_TEXT_LEN]
            else:
                short_text = self.text[:SHORT_TEXT_LEN]
                space = short_text.rfind(' ')
                return short_text[:space]

    def comments_count(self):
        p = Comment.objects.all().filter(article_id = self.id)
        return len(p)

    def lang(self):
        if Article.comments_count(self) % 10 != 1:
            return "s"
        else:
            return ""


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    text = models.TextField(blank=True)
    article = models.ForeignKey(Article, null=True, blank=True)
    approved = models.NullBooleanField()

    def __str__(self):
        return self.text
