from rest_framework import serializers
from .models import Movie, Review, Favorite

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('Title', 'Year', 'Released', 'Runtime', 'Genre', 'Director')

class ReviewSerializer(serializers.ModelSerializer):
    Movie = MovieSerializer(many=False)
    class Meta:
        model = Review
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.Content = validated_data.get('Content', instance.Content)
        instance.Star = validated_data.get('Star', instance.Star)
        instance.save()

        return instance

class FavoriteSerializer(serializers.ModelSerializer):
    Movies = MovieSerializer(many=True)
    class Meta:
        model = Favorite
        fields = '__all__'


        