from django.conf.urls import url, include
# from django.contrib.auth.decorators import login_required

from .views import( ActividadListView,
	                ActividadCreateView,
	                ActividadUpdateView,
	                ActividadDeleteView,
	                #API Vistas
	                ActividadListaAPIView,
	                ActividadCreateAPIView,
	                ActividadtUpdateAPIView,
	                ActividadDestroyAPIView,
	                ActividadList)

urlpatterns = [    
    url(r'^add$', (ActividadCreateView.as_view()), name='adicionar_actividad'),
    url(r'^lst$', (ActividadListView.as_view()), name='listar_actividad'),
    url(r'^upd/(?P<pk>\d+)/$', (ActividadUpdateView.as_view()), name='editar_actividad'),
    url(r'^dlt/(?P<pk>\d+)/$',ActividadDeleteView.as_view(), name='eliminar_actividad'),
    # urls de las APIS CON REST FRAMEWORK
    url(r'^dlt-api/(?P<pk>\d+)/$',ActividadDestroyAPIView.as_view()),
    url(r'^upd-api/(?P<pk>\d+)/$',ActividadtUpdateAPIView.as_view()),
    url(r'^add-api$',ActividadCreateAPIView.as_view()),
    url(r'^lstapi$',ActividadListaAPIView.as_view(), name="lstapi"),
    url(r'^lstaapi$',ActividadList.as_view(), name="lstaapi"),
    	
]
