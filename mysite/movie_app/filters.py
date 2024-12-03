from django_filters import FilterSet
from .models import Movie

from .models import Movie
from django_filters import FilterSet


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['gt', 'lt'],
            'country': ['exact'],
            'genre': ['exact'],
            'movie_status': ['exact'],
            'actor': ['exact'],
            'director': ['exact']
        }
