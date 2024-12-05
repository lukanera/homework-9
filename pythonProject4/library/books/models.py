from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    rating = models.IntegerField(default=0)