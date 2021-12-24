"""Patients model."""

# Django
from django.db import models

# Models
from hospital.users.models import User

# Utilities
from hospital.utils.models import BaseModel


class Patient(BaseModel):
    """Patient model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Paciente"
    )