from django import forms
from .models import HorarioClass, DIAS
# from django.forms import *
from django.db import models
from django.contrib.admin import widgets


class HorarioForm(forms.ModelForm):

	class Meta:
		model = HorarioClass

		fields = [
			'dia_inicio',
			'dia_fin',
			'hora_inicio',
			'hora_fin'
		]

		labels = {
			'dia_inicio': 'Dia Inicio',
			'dia_fin': 'Dia Fin',
			'hora_inicio': 'Hora Inicio',
			'hora_fin': 'Hora Final'
		}

		widgets = {
			'dia_inicio': forms.Select(choices=DIAS,attrs={'class':'form-control form-control-sm  ','required': True}),
			'dia_fin':forms.Select(choices=DIAS,attrs={'class':'form-control form-control-sm  '}),
			
			'hora_inicio':  forms.TextInput(attrs={'class':'form-control form-control-sm timeinput','required': True, 'placeholder':'9:00'}),
			'hora_fin': forms.TextInput(attrs={'class':'form-control form-control-sm  timeinput','required': True, 'placeholder':'17:00'}),
		}



	# 		