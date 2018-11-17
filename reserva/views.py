from django.shortcuts import render
from django.http import HttpResponse

def reserva(request):
	data = {}
	template = "aaaa.html"
	return render(request, template, data)