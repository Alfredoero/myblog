from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

