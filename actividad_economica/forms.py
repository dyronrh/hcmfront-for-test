from django import forms
from django.forms import widgets
from .models import ActividadEconomicaClass

class ActividadEconomicaForm(forms.ModelForm):
    class Meta:
        model = ActividadEconomicaClass
        fields = ['actividad']
        widgets = {
            'actividad': forms.TextInput(attrs={'class':' form-control form-control-md'})
        }