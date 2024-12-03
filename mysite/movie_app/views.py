from .serializers import *
from .models import *
from rest_framework import viewsets
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .permissions import CheckStatus,CheckAuthorHistory,CheckStatusActor

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers



class CountryViewSet(viewsets.ModelViewSet):
    queryset =Country.objects.all()
    serializer_class =CountrySerializers


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class =GenreSerializers

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class =ActorSerializers
    permission_classes = [CheckStatusActor]




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers



class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers
    permission_classes = [CheckAuthorHistory]



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [CheckStatusActor]






class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializers


class MovieListViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['movie_name', 'year']




class MovieDetailViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers
    permission_classes = [CheckStatus]

