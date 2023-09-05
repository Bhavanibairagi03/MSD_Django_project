from django import forms
from .models import Geeks

class GeekForm(forms.ModelForm):
    class Meta:
        model=Geeks
        fields="__all__"
        labels={'img':''}