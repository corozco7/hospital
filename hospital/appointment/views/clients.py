"""Clients view."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/main.html'