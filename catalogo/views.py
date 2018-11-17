from django.shortcuts import render
from django.http import HttpResponse

def catalogo(request, tipo_catalogo):
	data = {}
	template = "catalogo.html"
	data['catalogo'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = Bicicleta.objects.all()
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = Equipamiento.objects.all()
		data['objetos'] = equipamientos
	return render(request, template, data)