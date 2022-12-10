from django import forms
from django.forms import ModelForm
from .models import Csv_data


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv_data
        fields = ('file_name',)

