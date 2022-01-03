"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Utilities
from hospital.base.data import DocumentTypeOptions, GenderOptions
from hospital.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, modify some fields and
    add some extra fields.
    """

    first_name = models.CharField(max_length=150, verbose_name="Nombre")
    last_name = models.CharField(max_length=150, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo")
    password = models.CharField(max_length=150, verbose_name="Contraseña")
    document_type = models.CharField(
        max_length=2,
        choices=DocumentTypeOptions.choices,
        default=DocumentTypeOptions.CITIZEN_CARD,
        verbose_name="Tipo de documento"
    )
    document_number = models.CharField(
        unique=True,
        max_length=150,
        verbose_name="Numero de documento"
    )
    birthdate = models.DateField(null=True, verbose_name="Fecha de nacimiento")
    gender = models. CharField(
        max_length=1,
        choices=GenderOptions.choices,
        verbose_name="Genero"
    )
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        username = self.first_name[0] + self.last_name [1:]

        us = User.objects.filter(username=username)

        if(us.exists()):
            us = User.objects.filter(username__contains=username)
            username += str(us.count())

        self.username = username
        super(User, self).save(*args, **kwargs)