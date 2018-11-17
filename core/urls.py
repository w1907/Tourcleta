from django.urls import path
from core import views

urlpatterns = [
	path('dashboard/', views.index, name="core.index"),
]