from django.contrib import admin
from pacientes.models import Medico, Hospitales, ArchivosInterpretacion, Interpretaciones, Paciente


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    fields = ()

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    fields = ()


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Hospitales)
admin.site.register(ArchivosInterpretacion)
admin.site.register(Interpretaciones)
admin.site.register(Paciente, PacienteAdmin)