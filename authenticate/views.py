from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def signin(request):
	data = {}
	template = "signin.html"
	logout(request)
	username = password = ""
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('core.index'))
			else:
				messages.warning(request, "Correo o contraseña invalidos")
		else:
			messages.warning(request, "Correo o contraseña invalidos")
	return render(request, template, data)