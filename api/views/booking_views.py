from rest_framework import generics, permissions

from api.models.booking_model import Booking
from api.serializers.booking_serializers import BookingSerializer
from api.permissions import booking_permissions



class AllBookings(generics.ListCreateAPIView):

    """API View for Booking Model."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



class UpdateDeleteBookingAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API View for getting a single booking object."""
    permission_classes = (booking_permissions.IsOwnerOrReadOnly,)
    serializer_class = BookingSerializer

    def get_object(self):
        return Booking.objects.get(id=self.kwargs.get('pk'))