from django.db import models
from actividad_economica.models import ActividadEconomicaClass
from horario.models import HorarioClass
from django.db.models import Q
# Create your models here.

# Diccionario de tipos de tipos de jornadas para al parametro obciones(choices) del campo "tipo"
TIPO_JORNADA = (
    ('COM','Jornada Completa'),
    ('PAR','Jornada Parcial'),
    ('180','180 horas mensuales'),
    ('45H','45 horas semanales'),
    ('60H','60 horas semanales'),
    ('ADT','Autorizada por la Dirección del Trabajo'),
    ('JBI','Bisemanal'),
    ('JRA','Registro de Asistencia'),

	)
# Diccionario de tipos de empresa para al parametro obciones(choices) del campo "tipo_empresa"

TIPO_EMPRESA = (
	('ME', 'Micro Empresa'),
	('PE', 'Pequena Empresa'),
	('ME', 'Mediana Empresa'),
	('GE', 'Gran Empresa'))
# Lista de regiones para pasarla al parametro obciones(choices) del campo "region"
REGION = (
	('RAP','Arica y Parinacota'),
	('RTP','Tarapacá'),
	('RAN','Antofagasta'),
	('RAT','Atacama'),
	('RCO','Coquimbo'),
	('RVA','Valparaíso'),
	('RME','Metropolitana'),
	('ROH','O’Higgins'),
	('RMA','Maule'),
	('RBI','Biobío'),
	('RAR','Araucanía'),
	('RLR','Los Ríos'),
	('RLL','Los Lagos'),
	('RLL','Aysén'),
	('RMG','Magallanes'),
	)




class JornadaQuerySet(models.query.QuerySet):
   
    def search(self, query):
        lookups =  (Q(descripcion__icontains=query)  
        #            Q(tipo_empresa__icontains=query) | 
        #            Q(region__icontains=query) |
        #            Q(actividad_economica__icontains=query) 
                   )
        return self.filter(lookups).distinct()

class JornadaManager(models.Manager):
    def get_queryset(self):
        return JornadaQuerySet(self.model, using= self._db)
    
    def all(self):
        return self.get_queryset()
   
    def search(self,query):
        return self.get_queryset().search(query)

# Creando el Modelo Jornada
class JornadaClass(models.Model):
	#campo tipo de jornada, de timpo Char y cantidad maxima de caracteres 6
	tipo = models.CharField(max_length=3,choices=TIPO_JORNADA,default=TIPO_JORNADA[0])
	# descripcion de la jornada de trabajo
	descripcion = models.CharField(max_length=120, null=True,blank=True)
	# campo tipo de empresa de tipo char, longitud maxima de 2 caracteres
	tipo_empresa = models.CharField(max_length=2,choices=TIPO_EMPRESA,default=TIPO_EMPRESA[0])
	# campo region de la jornada, de tipo char longitud maxima de 2
	region = models.CharField(max_length=3, choices=REGION, default=REGION[0])
	# campo actividad_economica para declarar una relacion uno a muchos(una Jornada tiene una Actividad Economica
	# y una acividad economica puede estar registrada en varias Jornadas)
	actividad_economica = models.ForeignKey(ActividadEconomicaClass,on_delete=models.CASCADE,blank=True,null=True)
	# Lista de horarios de la jornada relacion muchos a muchos
	horario = models.ManyToManyField(HorarioClass)

	objects = JornadaManager()
