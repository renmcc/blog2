from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogArticles(models.Model):
    """
    models.CASCADE：级联删除，User对象删除文章也删除
    related_name：允许User类通过blog_posts反查BlogArticles
    """
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title