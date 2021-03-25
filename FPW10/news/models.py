from django.db import models


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

    def __str__(self):
        return f'{self.title.title()}: {self.body[:20]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'