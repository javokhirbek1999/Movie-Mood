from django.db import models


class Event(models.Model):

    """
    Event model:

    Fields:
        - movie    <-- linked to Movie model through Foreign key
        - description 
        - event_date
        - ticket_price 
        - venue 
    """

    movie = models.ForeignKey('api.Movie', on_delete=models.CASCADE)
    description = models.TextField()
    event_date = models.DateTimeField()
    ticket_price = models.DecimalField(decimal_places=2, max_digits=100)
    venue = models.CharField(max_length=200)


    @property
    def get_movie_details(self):
        return {
            'title': self.movie.title,
            'description': self.movie.description,
            'released_date': self.movie.released_date
        }
    

    def __str__(self) -> str:
        return f'Movie: {self.movie.title} | Date: {self.event_date}'
    