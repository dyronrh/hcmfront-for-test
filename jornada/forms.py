from django import forms
from django.db import models
from django.forms import widgets
from .models import JornadaClass, TIPO_EMPRESA,TIPO_JORNADA,REGION
from horario.models import HorarioClass

#declarando la clase JornadaForm que hereda de la clase Form
class JornadaForm(forms.ModelForm):
    class Meta:
        model = JornadaClass

        fields = [
          'tipo',
          'descripcion',
          'tipo_empresa',
          'region',
          'actividad_economica',
          'horario'
        ]

        labels = {
          'tipo': 'Tipo de Jornada',
          'descripcion': 'Descripcion',
          'tipo_empresa': 'Tipo de Empresa',
          'region': 'Region',
          'actividad_economica': 'Actividad Economica',
          'horario': 'Horario',
        }
        widgets = {
          'tipo': forms.Select(choices=TIPO_JORNADA, attrs={'class':'form-control form-control-sm' }),
          'descripcion': forms.Textarea( attrs={'class':'form-control form-control-sm' }),
          'tipo_empresa': forms.Select(choices=TIPO_EMPRESA, attrs={'class':'form-control form-control-sm '}),
          'region': forms.Select(choices=REGION,attrs={'class':'form-control form-control-sm '}),
          'actividad_economica': forms.Select(attrs={'class':'form-control form-control-sm '}),
          # 'horario': forms.ModelMultipleChoiceField(queryset=HorarioClass.objects.all())
          'horario': forms.CheckboxSelectMultiple(attrs={'class':'form-control form-control-sm '})
        }
    

			

			

