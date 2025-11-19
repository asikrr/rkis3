from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(default="default.jpg", upload_to='avatars/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)