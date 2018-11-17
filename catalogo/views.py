from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import bicicleta, equipamiento

def catalogo(request, tipo_catalogo):
	data = {}
	template = "catalogo.html"
	data['catalogo'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = bicicleta.objects.all()
		print(bicicletas)
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = equipamiento.objects.all()
		data['objetos'] = equipamientos
	print(data['catalogo'])
	return render(request, template, data)