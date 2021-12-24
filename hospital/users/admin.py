"""User admin classes."""

# Django
from django.contrib import admin

# Models
from hospital.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""
    list_display = ('username', 'first_name', 'last_name')