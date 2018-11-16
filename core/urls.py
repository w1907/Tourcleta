from django.urls import path
from core import views

urlpatterns = [
	path('user', views.index_usuario, name="core.index_usuario"),
	path('employee', views.index_empleado, name="core.index_empleado"),
	path('administrator', views.index_admin, name="core.index.admin"),
]