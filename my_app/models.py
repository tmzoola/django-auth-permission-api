from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE)