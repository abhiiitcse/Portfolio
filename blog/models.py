from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Postcategorymap(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    