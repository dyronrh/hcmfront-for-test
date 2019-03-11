from django.db import models

# Creando el modelo Actividad economica.
class ActividadEconomicaClass(models.Model):
	actividad = models.CharField(max_length=50,null=True, blank=True)

	def __str__(self):
		return self.actividad

		