from django import forms
from django.forms import ModelForm
from .models import Csv_data


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv_data
        # fields = ('file_name',)
        fields = ['file_name',]
        ##form = ('file_name',)

class CsvFileForm(CsvForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    class Meta(CsvForm.Meta):
        fields = CsvForm.Meta.fields + ['file',]
