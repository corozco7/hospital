"""Appointment admin classes."""

# Django
from django.contrib import admin

# Models
from hospital.appointment.models import Doctor, Patient


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Doctor admin."""
    list_display = ('user', 'specialty')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient admin."""
    list_display = ('user',)