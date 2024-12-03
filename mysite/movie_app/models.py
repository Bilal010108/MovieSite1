from django.db import models
from django .contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)



class Profile(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(16),
                                           MaxValueValidator(50)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    status = models.CharField(max_length=17,choices=STATUS_CHOICES,default='simple')

    def __str__(self):
       return f'{self.first_name},{self.last_name}'


class Country(models.Model):
   country_name = models.CharField(unique=True,max_length=32)

   def __str__(self):
       return self.country_name

class Director(models.Model):
    director_name =models.CharField(max_length=32,unique=True)
    director_bio = models.TextField()
    director_age = models.PositiveIntegerField(validators=[MinValueValidator(16),
                                           MaxValueValidator(60)])
    director_image = models.ImageField(upload_to='director_image',null=True,blank=True)



    def __str__(self):
        return self.director_name



class Actor(models.Model):
    actor_name = models.CharField(unique=True, max_length=20)
    actor_bio = models.TextField()
    actor_age =models.PositiveIntegerField(validators=[MinValueValidator(16),
                                                 MaxValueValidator(60)])
    actor_image =models.ImageField(upload_to='actor_image/',null=True,blank=True)

    def __str__(self):
        return self.actor_name

class Genre(models.Model):
    genre_name =models.CharField(unique=True,max_length=20)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_name =models.CharField(max_length=32)
    year = models.DateField()
    country= models.ManyToManyField(Country)
    director=models.ManyToManyField(Director)
    actor =models.ManyToManyField(Actor)
    genre=models.ManyToManyField(Genre)
    TYPE_CHOICES =(
        ('144','144'),
        ('360','360'),
        ('480','480'),
        ('720','720'),
        ('1080','1080'),
    )
    types = MultiSelectField(max_length=32,choices=TYPE_CHOICES,max_choices=5)
    movie_time = models.PositiveIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/',null=True,blank=True)
    movie_image  = models.ImageField(upload_to='movie_image/',null=True,blank=True)
    movie_status =models.CharField(max_length=16,choices=STATUS_CHOICES)


    def __str__(self):
        return self.  movie_name


    def get_avg_rating(self):
        ratings=self.comments.all()
        if ratings.exists():
         return round(sum(i.stars for i in  ratings) / ratings.count(),1)
        return 0

class MovieLanguages(models.Model):
    language =models.CharField(max_length=32)
    video =models.FileField(upload_to='movie_languages',null=True,blank=True)
    movie= models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie_languages')

    def __str__(self):
         return self.language


class Moments(models.Model):
  movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
  movie_moments = models.ImageField(upload_to='  movie_moments/',null=True,blank=True)

class Rating(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE )
    movie= models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    stars = models.IntegerField(choices=[(i,str(i))for i in  range(1,11)])
    parent= models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user


class Favorite(models.Model):
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    created_date =models.DateField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart =models.ForeignKey(Favorite,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)


class History(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    viewed_at=models.DateField(auto_now_add=True)
