from django.forms.widgets import DateInput as DjangoDateInput


class DateInput(DjangoDateInput):
    input_type = "date"