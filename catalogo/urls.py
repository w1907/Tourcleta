from django.urls import path
from catalogo import views

urlpatterns = [
	path('<str:tipo_catalogo>', views.catalogo, name="view.catalogo"),
]