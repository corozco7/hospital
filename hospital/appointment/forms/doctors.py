"""Doctors forms."""

# Django
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Models
from hospital.appointment.models import Doctor
from hospital.users.models import User

# Utils
from hospital.base.data import SpecialtyOptions
from hospital.base.widgets import DateInput


class DoctorForm(forms.ModelForm):
    """Doctor model form."""

    specialty = forms.ChoiceField(choices=SpecialtyOptions.choices, label="Especialidad")

    class Meta:
        """"Form settings."""

        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
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
        super(DoctorForm, self).save(*args, **kwargs)
        user = User.objects.filter(document_number=self.clean()["document_number"])
        doctor = Doctor.objects.create(user=user.first(), specialty=self.clean()["specialty"])
        doctor.save()
