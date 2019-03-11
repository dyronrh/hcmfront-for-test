from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import JornadaClass, REGION
from .forms import JornadaForm
from .serializers import JornadaSerializer
#importacion de las dependecias de DRF
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics   #importando vista genericas de RestFramework
# Creaando las vistas.

#Lista de jornadas
class JornadaListView(generic.ListView):
	model = JornadaClass
	template_name = 'jornada/lista_jornada.html'
	def get_context_data(self, **kwargs):
	    context = super(JornadaListView, self).get_context_data(**kwargs)
	    context['regiones'] = REGION
	    return context


class JornadaCreateView(generic.CreateView):
	model = JornadaClass
	form_class = JornadaForm
	template_name = 'jornada/form_jornada.html'
	success_url = reverse_lazy('jornada:listar_jornadas')


class JornadaUpdateView(generic.UpdateView):
	model = JornadaClass
	form_class = JornadaForm
	template_name = 'jornada/form_jornada.html'
	success_url = reverse_lazy('jornada:listar_jornadas')
		
class JornadaDeleteView(generic.DeleteView):
	model = JornadaClass
	template_name = 'jornada/eliminar_jornada.html'
	success_url = reverse_lazy('jornada:listar_jornadas')


'''
creando las visas de las APIS
'''

#vista listar y crear, vista generica basada en clase
class JornadaListaAPIView(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	queryset = JornadaClass.objects.all()
	serializer_class = JornadaSerializer


class JornadaCreateAPIView(generics.CreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = JornadaClass.objects.all()
	serializer_class = JornadaSerializer

class JornadaDestroyAPIView(generics.DestroyAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = JornadaClass.objects.all()
	serializer_class = JornadaSerializer

class JornadaUpdateAPIView(generics.UpdateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = JornadaClass.objects.all()
	serializer_class = JornadaSerializer

