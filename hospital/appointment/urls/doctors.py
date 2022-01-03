"""Doctor URLs."""

# Django
from django.urls import path

# Views
from hospital.appointment.views import doctors as doctors_views


urlpatterns = [
    path(
        route='create/',
        view=doctors_views.CreateDoctorView.as_view(),
        name='create'
    )
]