from django.contrib import admin
from .models import Movie, Review, Favorite

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Favorite)
