from django.contrib import admin
from .models import NucleoIncubador, Servidor
# Register your models here.


class NucleoIncubadorAdmin(admin.ModelAdmin):
    empty_value_display = 'Nenhum'
    list_display = ('name',)
    search_fields = (['name',])

admin.site.register(NucleoIncubador,NucleoIncubadorAdmin)
admin.site.register(Servidor)
