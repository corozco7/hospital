"""Appointment admin classes."""

# Django
from django.contrib import admin

# Models
from hospital.appointment.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Doctor admin."""
    list_display = ('user', 'specialty')