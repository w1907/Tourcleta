from django.urls import path
from catalogo import views

urlpatterns = [
	path('<str:tipo_catalogo>', views.catalogo, name="view.catalogo"),
	path('<str:tipo_catalogo>/<str:ver_mas>/<int:pk>', views.ver_mas, name="view.ver_mas"),
] 