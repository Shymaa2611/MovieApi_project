from django.urls import path
from . import views
urlpatterns=[
 path('',views.MoviesData.as_view(),name='movie')
]
