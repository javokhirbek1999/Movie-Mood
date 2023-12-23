from django.urls import path

from api.views import event_views


app_name = 'events'


urlpatterns = [
    path('', event_views.AllEvents.as_view(), name='events'),
    path('<int:pk>/', event_views.UpdateDeleteEventAPIView.as_view(), name='event'),
]