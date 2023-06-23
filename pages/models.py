from django.db import models

Rating={
    ('5','5 Start'),
    ('4','4 Start'),
    ('3','3 Start'),
    ('2','2 Start'),
    ('1','1 Start'),
}

Type={
    ('movie','movie'),
     ('series','series')
}
class Genre(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Movie(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    created=models.DateField()
    rate=models.CharField(max_length=20,choices=Rating)
    duration=models.CharField(max_length=10)
    genre=models.ForeignKey(Genre,on_delete=models.PROTECT)
    poster=models.ImageField()
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    type=models.CharField(max_length=50,choices=Type)
    def __str__(self):
        return self.title