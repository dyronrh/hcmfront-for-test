from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect


from django.views.generic import CreateView,DeleteView, UpdateView, ListView  #importando vistas genericas de Django
from rest_framework import generics   #importando vista genericas de RestFramework
from .models import ActividadEconomicaClass #importando modelo
from .forms import ActividadEconomicaForm   #importando Formulario
from .serializers import ActividadEconomicaSerializer
#============
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class ActividadListView(ListView):
	model = ActividadEconomicaClass
	template_name = 'actividad/lista_actividades.html'

class ActividadCreateView(CreateView):
	model = ActividadEconomicaClass
	form_class = ActividadEconomicaForm
	template_name = 'actividad/form_actividad.html'
	success_url = reverse_lazy('actividad:listar_actividad')

class ActividadUpdateView(UpdateView):
	model = ActividadEconomicaClass
	form_class = ActividadEconomicaForm
	template_name = 'actividad/form_actividad.html'
	success_url = reverse_lazy('actividad:listar_actividad')



class ActividadDeleteView(DeleteView):
	model = ActividadEconomicaClass
	template_name = 'actividad/eliminar_actividad.html'
	success_url = reverse_lazy('actividad:listar_actividad')


# creaando las API

class ActividadListaAPIView(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	queryset = ActividadEconomicaClass.objects.all()
	serializer_class = ActividadEconomicaSerializer


class ActividadCreateAPIView(generics.CreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = ActividadEconomicaClass.objects.all()
	serializer_class = ActividadEconomicaSerializer

class ActividadDestroyAPIView(generics.DestroyAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = ActividadEconomicaClass.objects.all()
	serializer_class = ActividadEconomicaSerializer

class ActividadtUpdateAPIView(generics.UpdateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = ActividadEconomicaClass.objects.all()
	serializer_class = ActividadEconomicaSerializer

class ActividadList(APIView):
    """
    Listar todas las Actividades, o crear una nueva.
    """
    def get(self, request, format=None):
        actividad = ActividadEconomicaClass.objects.all()
        serializer = ActividadEconomicaSerializer(actividad, many=True)
        authentication_classes = (SessionAuthentication, BasicAuthentication)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActividadEconomicaSerializer(data=request.data)
        serializer_context = {
            'request': request,
        }
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

