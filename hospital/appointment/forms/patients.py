"""Patients forms."""

# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Models
from ..models import Patient
from hospital.users.models import User

# Utilities
from hospital.base.widgets import DateInput


class PatientForm(forms.ModelForm):
    """patient model form."""

    class Meta:
        """Form settings."""

        model = User

        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'document_type',
            'document_number',
            'birthdate',
            'gender'
        )
        widgets = {
            'birthdate': DateInput()
        }
        error_messages = {
             'document_number': {
                 'unique': _("Este documento ya esta en uso.")
             }
        }

    def save(self, *args, **kwargs):
        super(PatientForm, self).save(*args, **kwargs)
        user = User.objects.filter(document_number=self.clean()["document_number"])
        patient = Patient.objects.create(user=user.first())
        patient.save()