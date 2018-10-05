from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.

def Index(request):
	ap= ""
	mensaje = ""
	if request.method == "POST":#_ificar si el formulario esta lleno
		form = UbicacionForm(request.POST)#instancia de la clase 
		if form.is_valid():#si el formulario es valido 
		   profesion = form.cleaned_data['profesion']
		   ciudad = form.cleaned_data['ciudad']#obtener el texto en el campo
		   ap = Profesionales.objects.filter(Q(profesion__icontains=profesion) & Q(ciudad__icontains=ciudad))
		if ap:
			pass
		else:
			mensaje = "No Hay Resultado Intenta De Nuevo"
	else:  
		form = UbicacionForm()#formulario vacio
	return render(request, 'index.html', locals())