from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myApp.models import Movie
from .serializers import MovieSerializer


class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer