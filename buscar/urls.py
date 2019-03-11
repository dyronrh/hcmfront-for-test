from django.conf.urls import url
from .views import BuscarList

urlpatterns = [
    url(r'^$',BuscarList.as_view(), name="query"),
]