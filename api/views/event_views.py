from rest_framework import generics, permissions

from api.serializers import event_serializers
from api.models.event_model import Event
from api.permissions import event_permissions


class AllEvents(generics.ListCreateAPIView):

    """API View for listing all available events and adding a new event."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = event_serializers.EventSerializer
    queryset = Event.objects.all()


class UpdateDeleteEventAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API View for single event object for get/update/delete/put operations."""

    permission_classes = (event_permissions.IsOwnerOrReadOnly,)
    serializer_class = event_serializers.EventSerializer

    def get_object(self):
        return Event.objects.get(id=self.kwargs.get('pk'))