from django import forms
from .models import Csv_data

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv_data
        fields = ('file_name',)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file =  forms.FileField()

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))