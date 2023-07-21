from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    shipping_cost = models.IntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} by {self.author.name}'
