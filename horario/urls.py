from django.conf.urls import url, include
from .views import (HorarioCreateView,HorarioListView,HorarioUpdateView,HorarioDeleteView,
	                HorarioListAPIView,HoraListaAPIView,HorarioAPI,HorarioCreateView,HorarioDeleteAPIView,HorarioUpdateAPIView)

urlpatterns = [    

    url(r'^add$', (HorarioCreateView.as_view()), name='adicionar_horario'),
    url(r'^lst', (HorarioListView.as_view()), name='listar_horarios'),
    url(r'^upd/(?P<pk>\d+)/$', (HorarioUpdateView.as_view()), name='editar_horario'),
    url(r'^dlt/(?P<pk>\d+)/$',HorarioDeleteView.as_view(), name='eliminar_horario'),
    # url(r'^api', HorarioList.as_view(), name='horario-list'),
    # urls de las APIS
    url(r'^lstapi',HorarioListAPIView.as_view(), name="lstapi"),
    url(r'^lstaapi',HorarioAPI.as_view(), name="lstaapi"),
    url(r'^add-api',HorarioCreateView.as_view(),name="add-api"),
    url(r'^upd-api/(?P<pk>\d+)/$',HorarioCreateView.as_view(),name="upd-api"),
    url(r'^dlt-api/(?P<pk>\d+)/$',HorarioDeleteAPIView.as_view(),name="dlt-api"),


]

