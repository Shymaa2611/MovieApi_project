from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify

class Movie(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    created_at=models.DateField(auto_now=True)
    duration=models.CharField(max_length=10)
    poster=models.ImageField(upload_to='movie/photo/',blank=True,null=True)
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    slug=models.SlugField(blank=True,null=True)
    def no_of_rating(self):
        no_ratings=Rating.objects.filter(movie=self).count()
        return no_ratings
    def avg_rating(self):
        sum_ratings=0
        ratings=Rating.objects.filter(movie=self)
        for rate in ratings:
            sum_ratings+=rate.stars
        count_value=Rating.objects.filter(movie=self).count()
        if count_value==0:
               count_value=1  
        return sum_ratings/count_value
    def __str__(self):
        return self.slug
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super(Movie,self).save(*args,**kwargs)
    
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    def __str__(self):
        return str(self.movie.title)
    class Meta:
        unique_together=(('user','movie'))
        index_together=(('user','movie'))


    
    