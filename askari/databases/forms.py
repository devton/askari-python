from django import forms
from .models import Database


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        exclude = ['user', 'organization']
