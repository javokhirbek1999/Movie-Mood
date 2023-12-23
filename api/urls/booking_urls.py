from django.urls import path

from api.views.booking_views import AllBookings, UpdateDeleteBookingAPIView


urlpatterns = [
    path('', AllBookings.as_view(), name='bookings'),
    path('<str:pk>/', UpdateDeleteBookingAPIView.as_view(), name='booking')
]