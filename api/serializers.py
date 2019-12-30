from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Review, Favorite

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

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


        