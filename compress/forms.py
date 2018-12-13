from .models import Compress
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Compress
        fields = ('image',)
