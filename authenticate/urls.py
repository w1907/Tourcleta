from django.urls import path
from authenticate import views

urlpatterns = [
	path('signin/', views.signin, name="authenticate.signin"),
	path('signout/', views.signout, name="authenticate.signout"),
	path('register/', views.register, name="authenticate.register")
]