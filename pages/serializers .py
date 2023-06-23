from rest_framework import serializers
from .models import Movie,Genre

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class MovieSeializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
