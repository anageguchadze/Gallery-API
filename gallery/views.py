from rest_framework import viewsets
from .serializers import ArtistSerializer, ArtworkSerializer, ExhibitionSerializer
from .models import Artist, Artwork, Exhibition
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .filters import ArtWorkFilter

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

class ArtWorkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    filterset_class = ArtWorkFilter
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['artist', 'creation_date']

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]