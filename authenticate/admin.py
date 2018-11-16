from django.contrib import admin
from authenticate.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'telefono', 'is_empleado')