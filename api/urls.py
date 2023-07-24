from django.urls import path
from . import views
urlpatterns=[
 path('',views.MoviesData.as_view(),name='movie'),
 path('Movie<int:id>/',views.MovieData_pk.as_view(),name='movie_pk'),
 path('api/rate/<int:pk>/',views.movie_rate,name='rate'),
 path('api/search/',views.seach_about_movie,name='search'),
]
