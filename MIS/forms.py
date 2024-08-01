from django import forms
from .models import Cppp, Gem, Offline, Consultancy


class CpppForm(forms.ModelForm):
    class Meta:
        model = Cppp
        fields = '__all__'


class GemForm(forms.ModelForm):
    class Meta:
        model = Gem
        fields = '__all__'


class OfflineForm(forms.ModelForm):
    class Meta:
        model = Offline
        fields = '__all__'


class ConsultancyForm(forms.ModelForm):
    class Meta:
        model = Consultancy
        fields = '__all__'
