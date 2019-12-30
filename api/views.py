from urllib import request
import requests
from .serializers import MovieSerializer, ReviewSerializer, FavoriteSerializer, UserSerializer
from .models import Movie, Review, Favorite
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import django_filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('Title', 'Genre')
    search_fields = ('Title', 'Genre')
    ordering_fields = ('id', 'Year')
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        if request.data.get("title"):
            title = request.data["title"]
        else:
            return Response(data={"Error": "Podaj tytuł filmu!"}, status=status.HTTP_400_BAD_REQUEST)

        url = f'http://www.omdbapi.com/?t={title}&apikey={settings.API_KEY}'
        response = requests.get(url)
        if response.status_code == requests.codes.ok and response.json()['Response'] == 'True':
            if not Movie.objects.filter(Title=response.json()['Title']).exists():
                serializer = MovieSerializer(data=response.json())
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(data={"Error": "Błąd!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                movie_from_database = Movie.objects.get(Title=response.json()['Title'])
                movie_from_database_serialized = MovieSerializer(movie_from_database)
                return Response(movie_from_database_serialized.data)
        else:
            return Response(data={"Error": "Nie ma takiego filmu!"}, status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_fields = ('Author', 'Movie')

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_fields = ('Author')


