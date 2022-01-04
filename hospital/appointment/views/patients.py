"""Patients view."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse

# Forms
from ..forms import PatientForm


class CreatePatientView(LoginRequiredMixin, CreateView):
    """Create a patient."""
    template_name = 'patients/new.html'
    form_class = PatientForm

    def get_success_url(self):
        return reverse('patients:create')