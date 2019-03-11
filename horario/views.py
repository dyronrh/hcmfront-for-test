
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .models import HorarioClass
from .forms import HorarioForm
from django.views import generic
# API desarrollos de vistas
from .serializers import HorarioSerializer
from rest_framework import viewsets,generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Crear las vistas a continuacion.


class HoraListaAPIView(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	queryset = HorarioClass.objects.all()
	serializer_class = HorarioSerializer


class HorarioListView(generic.ListView):
	"""creando la vista basada en clase HorarioListView"""
	model = HorarioClass
	template_name = 'horario/lista_horario.html'

class HorarioCreateView(generic.CreateView):
	"""creando la vista basada en clase HorarioCreateView"""
	model = HorarioClass
	form_class =HorarioForm
	template_name = 'horario/form_horario.html'
	success_url = reverse_lazy('horario:listar_horarios')

class HorarioUpdateView(generic.UpdateView):
	"""creando la vista basada en clase HorarioUpdateView"""
	model = HorarioClass
	form_class = HorarioForm
	template_name = 'horario/form_horario.html'
	success_url = reverse_lazy('horario:listar_horarios')

class HorarioDeleteView(generic.DeleteView):
	"""creando la vista basada en clase HorarioDeleteView"""
	model = HorarioClass
	template_name = 'horario/eliminar_horario.html'
	success_url = reverse_lazy('horario:listar_horarios')
	
#CREACION DE LAS APIS 	basadas en clases

class HorarioListAPIView(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = HorarioClass.objects.all()
	serializer_class = HorarioSerializer

# creando la vista de la API actualizar horario

class HorarioUpdateAPIView(generics.UpdateAPIView):
	authentication_classes  = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = HorarioClass.objects.all()
	serializer_class = HorarioSerializer


class HorarioDeleteAPIView(generics.DestroyAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = HorarioClass.objects.all()
	serializer_class = HorarioSerializer



class HorarioAPI(APIView):
    """
    Listar todas las Actividades, o crear una nueva.
    """
    def get(self, request, format=None):
        actividad = HorarioClass.objects.all()
        serializer = HorarioSerializer(actividad, many=True)
        authentication_classes = (SessionAuthentication, BasicAuthentication)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HorarioSerializer(data=request.data)
        serializer_context = {
            'request': request,
        }
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

