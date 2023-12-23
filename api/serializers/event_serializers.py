from rest_framework import serializers

from api.models import event_model


class EventSerializer(serializers.ModelSerializer):

    """Event Serializer for Event model."""

    class Meta:
        model = event_model.Event
        fields = ('id', 'movie', 'get_movie_details', 'description', 'event_date', 'ticket_price', 'venue')
        extra_kwargs = {
            'movie': {'write_only': True}
        }

    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
