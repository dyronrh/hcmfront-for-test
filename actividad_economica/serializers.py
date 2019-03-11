from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import ActividadEconomicaClass



#creando clase Serializer

class ActividadEconomicaSerializer(ModelSerializer):
	class Meta:
		model = ActividadEconomicaClass
		fields = '__all__'
