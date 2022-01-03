"""Doctors view."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse

# Forms
from ..forms import DoctorForm


class CreateDoctorView(LoginRequiredMixin, CreateView):
    """Create a doctor."""
    template_name = 'doctors/new.html'
    form_class = DoctorForm

    def get_success_url(self):
        return reverse('doctors:create')