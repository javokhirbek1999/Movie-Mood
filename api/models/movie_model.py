from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    
    """
    Movie model:

    Fields:
        - title
        - description
        - released date
    """

    title = models.CharField(max_length=200, unique=True)
    slug_title = models.SlugField(max_length=200, default="")
    description = models.TextField()
    released_date = models.DateField()

    @property
    def get_movie_reviews(self):
        all_reviews = []

        for review in Review.objects.filter(movie__id=self.id):
            current_formatted_review = {
                'user': review.get_user_details,
                'content': review.content,
                'rate': review.rate,
            }

            all_reviews.append(current_formatted_review)

        return all_reviews
        

    def __str__(self) -> str:
        return self.title


class Review(models.Model):

    """
    Review model:

    Fields: 
        - user
        - movie
        - content
        - rate
    """

    def validate_min_max_rate(rate):
        if not (1 <= rate <= 5):
            raise ValidationError(
                _("Rate %(rate) must be between 1 and 5"),
                params={"rate": rate}
            )

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    movie = models.ForeignKey('api.Movie', on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(validators=[validate_min_max_rate])


    @property
    def get_user_details(self):
        return {
            'email': self.user.email,
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }

    @property
    def get_movie_details(self):
        return {
            'title': self.movie.title,
            'description': self.movie.description,
            'slug_title': self.movie.slug_title,
            'released_date': self.movie.released_date
        }

