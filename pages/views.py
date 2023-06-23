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
class MovieData_pk(APIView):
     def get(self,request,id):
         movie_data=Movie.objects.get(id=id)
         data=MovieSerializers(movie_data)
         return Response(data.data)
     def put(self,request,id):
         movie_data=Movie.objects.get(id=id)
         data=MovieSerializers(movie_data,data=request.data)
         if data.is_valid():
             data.save()
         return Response(data.data)
     def delete(self,request,id):
         movie_data=Movie.objects.all(id=id)
         movie_data.delete()
         return Response(status=status.HTTP_204_NO_CONTENT) 