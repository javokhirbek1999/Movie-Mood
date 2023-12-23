from rest_framework import generics, permissions


from api.models.movie_model import Movie, Review
from api.serializers.movie_serializers import MovieSerializer, ReviewSerializer
from api.permissions import booking_permissions


class AllMovies(generics.ListCreateAPIView):
    
    """API View for listing all available movies and adding a new movie."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class UpdateDeleteMovieAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API View for single movie object for get/update/delete/put operations."""
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = MovieSerializer
    
    def get_object(self):
        return Movie.objects.get(slug_title=self.kwargs.get('slug'))


class AllReviews(generics.ListCreateAPIView):

    """API View for listing and adding a new review."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class UpdateDeleteReviewAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API View for a single review for get/update/delete/put operations."""

    permission_classes = (booking_permissions.IsOwnerOrReadOnly,)
    serializer_class = ReviewSerializer

    def get_object(self):
        return Review.objects.get(id=self.kwargs.get('id'))