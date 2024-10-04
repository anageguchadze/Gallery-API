import django_filters
from .models import Artwork

class ArtWorkFilter(django_filters.FilterSet):
    class Meta:
        model = Artwork
        fields = ['artist', 'creation_date']