from django import forms
from .models import Cppp, Gem


class CpppForm(forms.ModelForm):
    class Meta:
        model = Cppp
        fields = '__all__'


class GemForm(forms.ModelForm):
    class Meta:
        model = Gem
        fields = '__all__'
