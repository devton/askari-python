from django import forms
# from ..core.tags.utils import tags_for
from .models import Clip


class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip
        exclude = ['slug']

    # tags = forms.CharField(max_length=50, required=False)

    # def __init__(self, *args, **kwargs):
    #     super(ClipForm, self).__init__(*args, **kwargs)

    #     if self.instance.pk:
    #         self.initial['tags'] = tags_for(self.instance)
