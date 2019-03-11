from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import (JornadaCreateView,JornadaListView,JornadaUpdateView,JornadaDeleteView,
	               #vista de las APIS
                    JornadaCreateAPIView,JornadaDestroyAPIView,JornadaUpdateAPIView,JornadaListaAPIView
	               )

urlpatterns = [    
    url(r'^add$', JornadaCreateView.as_view(), name='adicionar_jornada'),
    url(r'^lst',JornadaListView.as_view(), name='listar_jornadas'),

    url(r'^upd/(?P<pk>\d+)/$',JornadaUpdateView.as_view(), name='editar_jornada'),
    url(r'^dlt/(?P<pk>\d+)/$',JornadaDeleteView.as_view(), name='eliminar_jornada'),
     # urls de las APIS CON REST FRAMEWORK
    url(r'^dlt-api/(?P<pk>\d+)/$',JornadaDestroyAPIView.as_view(),name='dlt-api'),
    url(r'^upd-api/(?P<pk>\d+)/$',JornadaUpdateAPIView.as_view(),name='upd-api'),
    url(r'^add-api$',JornadaCreateAPIView.as_view(),name='add-api'),
    url(r'^lista',JornadaListaAPIView.as_view(), name='lst-api'),
    ]
