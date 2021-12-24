"""Doctors model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from hospital.users.models import User

# Utilities
from hospital.utils.models import BaseModel


class Doctor(BaseModel):
    """Doctor model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Doctor"
    )

    class SpecialtyOptions(models.TextChoices):
        """Specialty options."""
        GENERAL_MEDICINE = 'GM', _('Medicina General')
    
    specialty = models.CharField(
        max_length=2,
        choices=SpecialtyOptions.choices,
        default=SpecialtyOptions.GENERAL_MEDICINE,
        verbose_name="Especialidad"
    )