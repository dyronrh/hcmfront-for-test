from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import HorarioClass


class HorarioSerializer(ModelSerializer):
	class Meta:
		model = HorarioClass
		fields = '__all__'

	