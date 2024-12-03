from rest_framework import serializers
from .models import *


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieListSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    director = DirectorSerializers(many=True)
    actor = ActorSerializers(many=True)
    avg_rating =serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = ['actor', 'movie_name', 'year', 'country', 'movie_image', 'director', 'genre', 'movie_status','avg_rating']

    def get_avg_rating(self,obj):
     return obj.get_avg_rating()


class MovieMoments(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
                model = Rating
                fields = '__all__'


class MovieDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    director = DirectorSerializers(many=True)
    actor = ActorSerializers(many=True)
    movie_languages = MovieLanguagesSerializers(many=True, read_only=True)
    comments =RatingSerializers(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'movie_trailer', 'movie_image', 'actor', 'director',
                  'types', 'movie_time', 'description', 'movie_status', 'movie_languages','comments']




class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields ='__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'