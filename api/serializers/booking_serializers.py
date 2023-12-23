from rest_framework import generics, serializers


from api.models.booking_model import Booking


class BookingSerializer(serializers.ModelSerializer):

    """Serializer for Booking model."""

    class Meta:
        model = Booking
        fields = ('id', 'user', 'get_user_details', 'event', 'get_event_details', 'total_tickets', 'status', 'get_total_price')
        extra_kwargs = {
            'user': {'write_only': True},
            'event': {'write_only': True},
        }
    
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)