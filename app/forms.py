from django import forms
from .models import SlangWord

class SlangForm(forms.ModelForm):
    class Meta:
        model = SlangWord
        fields = ['word', 'definition', 'image_url']
