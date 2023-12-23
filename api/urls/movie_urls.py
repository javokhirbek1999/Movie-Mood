from django.urls import path

from api.views import movie_views


app_name = 'movie'


urlpatterns = [
    path('', movie_views.AllMovies.as_view(), name='movies'),
    path('<str:slug>/', movie_views.UpdateDeleteMovieAPIView.as_view(), name='movie'),
    path('reviews/all', movie_views.AllReviews.as_view(), name='reviews'),
    path('reviews/<int:id>/', movie_views.UpdateDeleteReviewAPIView.as_view(), name='review')
]