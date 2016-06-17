from django.contrib import admin
from .models import Computer


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'positionID', 'occupied')


admin.site.register(Computer, ComputerAdmin)
