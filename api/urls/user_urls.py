from django.urls import path

from api.views import user_views


app_name = 'user'


urlpatterns = [
    path('create/', user_views.UserAPIView.as_view(), name='create-user'),
    path('user/<str:pk>', user_views.UpdateDeleteUserAPIView.as_view(), name='user'),
    path('all/', user_views.AllUsers.as_view(), name='all-users'),
    path('token/', user_views.AuthTokenAPIView.as_view(), name='token')
]