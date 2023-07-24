from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Movie(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    created_at=models.DateField(auto_now=True)
    duration=models.CharField(max_length=10)
    poster=models.ImageField(upload_to='movie/photo/',blank=True,null=True)
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    def __str__(self):
        return str(self.movie.title)
    class Meta:
        unique_together=(('user','movie'))
        index_together=(('user','movie'))


    
    