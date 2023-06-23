from django.shortcuts import render
from .models import Movie
from rest_framework.response import Response
from .serializers  import  MovieSerializers
from rest_framework import status
from rest_framework.decorators import APIView

class MoviesData(APIView):
      def get(self,request):
            Movies=Movie.objects.all()
            response=MovieSerializers(Movies,many=True).data
            return Response(response)
      def post(self,request):
         add_Movie=MovieSerializers(data=request.data)
         if add_Movie.is_valid():
             add_Movie.save()
             return Response(add_Movie.data,status=status.HTTP_201_CREATED)
         return Response(add_Movie.errors,status=status.HTTP_400_BAD_REQUEST)
    