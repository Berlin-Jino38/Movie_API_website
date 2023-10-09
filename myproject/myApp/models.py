from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    pic = models.ImageField(upload_to='images')
    hit_flop = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name
class Movie_detail(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='images')
    actor_name=models.CharField( max_length=50)  
    actress_name=models.CharField( max_length=50)
    details=models.CharField(max_length=256)
    