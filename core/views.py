from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	data = {}
	template = "core/index.html"
	return render(request, template, data)

def index_usuario(request):
	data = {}
	template = "core/index_usuario.html"
	return render(request, template, data)