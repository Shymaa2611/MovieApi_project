from django.urls import path
from . import views
urlpatterns=[
 path('Movie/',views.MoviesData.as_view(),name='movie'),
 path('Movie/<slug:slug>/',views.MovieData_pk.as_view(),name='movie_pk'),
 path('api/rate/<slug:slug>/',views.movie_rate,name='rate'),
 path('api/search/',views.seach_about_movie,name='search'),
 path('api/newmovie/',views.get_new_movie,name='newmovie'),
]
