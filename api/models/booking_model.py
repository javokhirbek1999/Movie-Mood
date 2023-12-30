from django.db import models
from django.contrib.auth import get_user_model


BOOKING_STATUS = (
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
    ('Booked', 'Booked')
)

class Booking(models.Model):

    """
    Event booking model
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey('api.Event', on_delete=models.CASCADE)
    total_tickets = models.IntegerField()
    status = models.CharField(max_length=50, choices=BOOKING_STATUS, default='Pending')

    @property
    def get_total_price(self):
        return self.event.ticket_price * self.total_tickets
    
    @property
    def get_user_details(self):
        return {
            'email': self.user.email,
            # 'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }
    
    @property
    def get_event_details(self):
        return {
            'movie': self.event.get_movie_details,
            'description': self.event.description,
            'event_date': self.event.event_date,
            'ticket_price': self.event.ticket_price,
            'venue': self.event.venue            
        }