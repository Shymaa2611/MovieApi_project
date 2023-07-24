from django.shortcuts import render
from .models import Movie,Rating
from rest_framework.response import Response
from .serializers  import  MovieSerializers,ratingSerializers
from rest_framework import status
from rest_framework.decorators import APIView,api_view
from django.contrib.auth.models import User

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
     def get(self,request,slug):
         movie_data=Movie.objects.get(slug=slug)
         data=MovieSerializers(movie_data)
         return Response(data.data)
     def put(self,request,slug):
         movie_data=Movie.objects.get(slug=slug)
         data=MovieSerializers(movie_data,data=request.data)
         if data.is_valid():
             data.save()
         return Response(data.data)
     def delete(self,request,slug):
         movie_data=Movie.objects.all(slug=slug)
         movie_data.delete()
         return Response(status=status.HTTP_204_NO_CONTENT) 
     

@api_view(['GET','post'])
def movie_rate(request, slug):

    if 'stars' in request.data:
            movie = Movie.objects.get(slug=slug)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                rating = Rating.objects.get(user=user, movie=movie.pk) 
                rating.stars = stars
                rating.save()
                serializer=ratingSerializers(rating, many=False)
                json = {
                    'message': 'movie Rate is Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                rating = Rating.objects.create(stars=stars, movie=movie, user=user)
                serializer=ratingSerializers(rating, many=False)
                json = {
                    'message': 'Movio Rate is Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

    else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_new_movie(request):
     movie=Movie.objects.all()
     new_movie=movie.order_by('-created_at')[:10]
     serializer=MovieSerializers(new_movie,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def seach_about_movie(request):
     data = Movie.objects.filter(
       title=request.data['title']
    )
     serializer=MovieSerializers(data,many=True)
     return Response(serializer.data)