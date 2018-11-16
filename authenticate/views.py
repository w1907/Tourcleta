from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from authenticate.forms import SignUpForm

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
				if user.profile.is_empleado:
					return HttpResponse("Soy Empleado")
				else:
					return HttpResponse("Soy Usuario normal")
			else:
				messages.warning(request, "Correo o contraseña invalidos")
		else:
			messages.warning(request, "Correo o contraseña invalidos")
	return render(request, template, data)

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('authenticate.signin'))

def register(request):
	template = 'register.html'
	if request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.telefono = form.cleaned_data.get('telefono')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('core.index'))
	else:
		form = SignUpForm()
	return render(request, template, {'form': form})