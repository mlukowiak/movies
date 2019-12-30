from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Movie(models.Model):
    Title = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)
    Released = models.CharField(max_length=100)
    Runtime = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)

    def __str__(self):
        return self.Title + " (" + str(self.Year) + ")"

class Review(models.Model):
    Content = models.TextField(default='')
    Star = models.IntegerField(default=5)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='Reviews')

    def __str__(self):
        return self.Content + " - " + str(self.Author)

class Favorite(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Movies = models.ManyToManyField(Movie)

    def __str__(self):
        return str(self.Author) + "'s' favorite movies" 