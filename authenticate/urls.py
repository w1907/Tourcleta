from django.urls import path
from authenticate import views

urlpatterns = [
	path('signin/', views.signin, name="authenticate.signin")
]