# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class DocumentTypeOptions(models.TextChoices):
        CITIZEN_CARD = "CC", _("Cedula de Ciudadania")
        ID_CARD = "TI", _("Tarjeta de Identidad")

class GenderOptions(models.TextChoices):
        MALE = "M" , _("Masculino")
        FEMALE = "F", _("Femenino")

class SpecialtyOptions(models.TextChoices):
        """Speciality options."""
        GENERAL_MEDICINE = 'GM', _('Medicina General')