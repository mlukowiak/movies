from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)
    Released = models.CharField(max_length=100)
    Runtime = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)

    def __str__(self):
        return self.Title
