from rest_framework import serializers
from .models import JornadaClass

class JornadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = JornadaClass
		fields = '__all__'