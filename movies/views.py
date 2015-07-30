from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MovieSerializer
from .models import MovieModel

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing movie instances.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()


class SearchAPIView(APIView):
    """
        APIView for search.Only get method is defined.
    """
    def get(self, request, movie_name):
        """takes movie_name as get parameter"""
        if movie_name:
            movies = MovieModel.objects.filter(name__icontains=movie_name)
            movies_serializer = MovieSerializer(movies, many=True)
            return Response(movies_serializer.data)
