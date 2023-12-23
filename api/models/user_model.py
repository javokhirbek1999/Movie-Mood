from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    """
    User Manager for Base User Model.

    Supports the following operations:
    
    1. Creating users
    2. Email validation
    """


    use_in_migrations = True

    def create_user(self, first_name, last_name, username, email, password=None, **kwargs: Any) -> Any:

        """Creates a new user model with email validation."""

        # Email validation
        if not email:
            raise ValueError(_('Email is required, please enter your email'))

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **kwargs)


        # Set password for user
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)

        return user
    

    def create_superuser(self, first_name, last_name, username, email, password):

        """Creates a new admin user."""

        user = self.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)


        # Admin users are activated by default
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):

    """Base custom User Model for all authentication and authorization."""


    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=200, unique=False, null=False, blank=False)
    last_name = models.CharField(max_length=200, unique=False, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
