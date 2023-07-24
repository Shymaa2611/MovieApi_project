from rest_framework import serializers
from .models import Movie,Rating

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
class ratingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

