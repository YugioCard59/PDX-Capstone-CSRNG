from django import forms
from django.forms import ModelForm
from .models import Token_storage, Token_user

class StorageForm(ModelForm):
    name = forms.TextInput(attrs={'id':'writeToDom'})
    name.render('writeToDom', "{{writeToDom}}")
    class Meta:
        model = Token_storage
        fields = ('token_value',)