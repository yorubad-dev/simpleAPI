from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=35)
    article_body = models.CharField(max_length=1500)
    email = models.EmailField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
