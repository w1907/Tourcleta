from django.urls import path
from arriendo import views

urlpatterns = [
    path('crear_arriendo/', views.crear_arriendo, name="crear_arriendo"),
]