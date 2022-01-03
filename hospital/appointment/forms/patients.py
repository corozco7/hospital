"""Patients forms."""

# Django
from django import forms
from django.forms import fields

# Models
from ..models import Patient


class PatientForm(forms.ModelForm):
    """patient model form."""

    pass