from django import forms
from django.forms import ModelForm
from .models import Csv_data

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __intit__(self, *args, **kwargs):
        #below calls the above class that sets multiple input true
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
# class FileFieldForm(forms.Form):

#     file_field = MultipleFileField()


class CsvForm(forms.ModelForm):
    #New added below above meta
    file_name = MultipleFileField(widget=MultipleFileInput(attrs={"allow_multiple_selected": True}))

   #_____

    class Meta:
        model = Csv_data
        fields = ('file_name',)
    

#BELOW IS ADDED TEST MULTI

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __intit__(self, *args, **kwargs):
#         #below calls the above class that sets multiple input true
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result
# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()

