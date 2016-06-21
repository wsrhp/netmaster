from django.contrib import admin
from .models import Computer


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('positionID', 'name', 'user', 'occupied')


admin.site.register(Computer, ComputerAdmin)
