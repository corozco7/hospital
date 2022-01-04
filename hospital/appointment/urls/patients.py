"""Patient URLs."""

# Django
from django.urls import path

# Views
from hospital.appointment.views import patients as patients_views


urlpatterns = [
    path(
        route='create/',
        view=patients_views.CreatePatientView.as_view(),
        name='create'
    )
]