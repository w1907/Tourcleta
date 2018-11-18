from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
	#path('', views.catalogo, name='view.catalogo'),
	path('bicicleta_list/', views.BicicletaList.as_view(), name='bicicleta_list'),
	path('<str:tipo_catalogo>', views.catalogo, name="view.catalogo"),
	path('<str:tipo_catalogo>/<str:ver_mas>/<int:pk>', views.ver_mas, name="view.ver_mas"),
	path('new/', views.BicicletaCreate.as_view(), name='bicicleta_new'),
	path('edit/<int:pk>', views.BicicletaUpdate.as_view(), name='bicicleta_edit'),
	path('delete/<int:pk>', views.BicicletaDelete.as_view(), name='bicicleta_delete'),
	
]
