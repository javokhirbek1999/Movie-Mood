from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from api.models.user_model import User
from api.models import movie_model, booking_model, event_model


@admin.register(User)
class UserAdminConfig(UserAdmin):

    ordering = ['id']
    list_filter = ['id']
    list_display = ['email', 'username', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )


@admin.register(movie_model.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug_title', 'description', 'released_date')
    prepopulated_fields = {'slug_title': ('title',),}

admin.site.register(event_model.Event)
admin.site.register(booking_model.Booking)
