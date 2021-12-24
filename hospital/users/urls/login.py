"""Login URLs."""

# Django
from django.urls import path

# Views
from hospital.users.views import login as login_views


urlpatterns = [
    path(
		route='login/',
		view=login_views.LoginView.as_view(),
		name='login'
	),
	path(
		route='logout/',
		view=login_views.LogoutView.as_view(),
		name='logout'
	)
]
