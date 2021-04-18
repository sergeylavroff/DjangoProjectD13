from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    rating = models.IntegerField(default = 0)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='news',)

    def __str__(self):
        return f'{self.title.title()}: {self.body[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscriber = models.ManyToManyField(User, blank=True, verbose_name='Подписчики')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'
