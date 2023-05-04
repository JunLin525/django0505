from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.


class ab:
    pass


class Practice(models.Model):
    name = models.CharField(max_length=50, default='undefined')
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        'CustomUser',  # 原本:auth.User
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'CustomUser', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments = models.CharField(max_length=140)
    author = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comments

    def get_absolute_url(self):
        return reverse("article_list")
