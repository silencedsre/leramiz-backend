from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    blog_image = models.ImageField(upload_to="img/blog")
    author = models.CharField(max_length=150)
    blog_time = models.DateTimeField()
    blog_headline = models.CharField(max_length=300, default=None)
    blog_article = models.TextField(blank=True)
    article_highlight = models.TextField(blank=True)

    def __str__(self):
        return self.blog_headline

    def get_absolute_url(self):
        return reverse(viewname='blog:detail', kwargs={'pk':self.pk})


    #for comments
class CommentModel(models.Model):
    author = models.CharField(max_length=150)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.author + " : " + self.comment