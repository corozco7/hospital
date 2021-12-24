"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Utilities
from hospital.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, add some extra fields.
    """

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']