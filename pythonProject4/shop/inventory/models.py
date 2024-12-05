from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10000, decimal_places=1000, default=0)
    stock_quanity = models.IntegerField(default=0)
    raiting = models.DecimalField(max_digits=10, decimal_places=10, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')