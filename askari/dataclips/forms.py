from django import forms
from .models import Clip


class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip
        exclude = ['slug']

    tags = forms.CharField(max_length=50, required=False)
