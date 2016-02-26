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
            return self.text