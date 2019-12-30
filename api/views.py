from urllib import request
import requests
from .serializers import MovieSerializer, ReviewSerializer, FavoriteSerializer
from .models import Movie, Review, Favorite
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

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

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


