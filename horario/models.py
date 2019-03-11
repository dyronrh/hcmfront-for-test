from django.db import models

# diccionario clave valor de los dias de la semana
DIAS = (
    ('Lu','LUNES'),
    ('Ma','MARTES'),
    ('Mi','MIERCOLES'),
    ('Ju','JUEVES'),
    ('Vi','VIERNES'),
    ('Sa','SABADO'),
    ('Do','DOMINGO'),
	)

# Create your models here.
class HorarioClass(models.Model):
	dia_inicio = models.CharField(max_length=2,choices=DIAS)
	dia_fin    = models.CharField(max_length=2,choices=DIAS, blank=True,null=True)
	hora_inicio= models.TimeField()
	hora_fin   = models.TimeField()

	def __str__(self):
		# retornando una cadena con el formato requerido de los valores ingresados de los horario y los dias
		return '{}-{} {}-{}'.format(self.dia_inicio, self.dia_fin, self.hora_inicio, self.hora_fin)

		