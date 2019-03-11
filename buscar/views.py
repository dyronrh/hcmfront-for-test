from django.shortcuts import render
from jornada.models import JornadaClass
from django.views.generic import ListView

# Creando las vistas de la app Buscar.
class BuscarList(ListView):
	# queryset = Product.objects.all()
	template_name = "buscar/views.html"
	paginate_by = 5

	def get_context_data(self,*args, **kwargs):
	    context = super(BuscarList, self).get_context_data(*args,**kwargs)
	    context['query'] = self.request.GET.get('q')
	    # SearchQuery.objects.create(query=query)
	    return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q',None)

		
		if query is not None:
			return JornadaClass.objects.search(query)
		return JornadaClass.objects.featured()

