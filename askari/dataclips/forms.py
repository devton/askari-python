from django import forms
from .models import Clip

class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip

