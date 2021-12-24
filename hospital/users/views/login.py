"""Users views."""

# Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(auth_views.LoginView):
	"""Login view."""

	template_name = 'login/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
	"""Logout view."""

	template_name = 'login/logged_out.html'
