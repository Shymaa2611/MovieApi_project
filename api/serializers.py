from rest_framework import serializers
from .models import Movie,Rating

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['title','description','created_at','duration','poster','director','language','no_of_rating','avg_rating']
class ratingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

