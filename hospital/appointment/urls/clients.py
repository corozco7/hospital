"""Client URLs."""

# Django
from django.urls import path

# Views
from hospital.appointment.views import clients as clients_views


urlpatterns = [
    path(
        route='',
        view=clients_views.TestView.as_view(),
        name='main'
    )
]