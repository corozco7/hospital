"""Doctors model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from hospital.users.models import User

# Utilities
from hospital.base.data import SpecialtyOptions
from hospital.utils.models import BaseModel


class Doctor(BaseModel):
    """Doctor model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    specialty = models.CharField(
        max_length=2,
        choices=SpecialtyOptions.choices,
        verbose_name="Especialidad"
    )