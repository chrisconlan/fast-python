
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=254, unique=True)

class Book(models.Model):
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=254, db_index=True)
    subtitle = models.CharField(max_length=254)
