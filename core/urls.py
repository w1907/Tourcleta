from django.urls import path
from core import views

urlpatterns = [
	path('', views.index, name="core.index"),
	path('', views.index_usuario, name="core.index.usuario"),
	path('', views.index_empleado, name="core.index.empleado"),
	path('', views.index_admin, name="core.index.admin")
]