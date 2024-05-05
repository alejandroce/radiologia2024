from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from pacientes.views import PacientesRegistrados, \
    EstudiosInterpretacion, RegistroPacientesView, EstudiosRegistrados,\
    PerfilPaciente, CrearInterpretacion, Detalle, EditarPaciente, Imprimir,\
    EditarInterpretacion, EstudiosDefaultList, EditarInterpretacionDefault,\
    EliminarPaciente, ImprimirExcel

admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', 'pacientes.views.index'),
    url(r'^cerrar/$', 'pacientes.views.cerrar', name='cerrar'),
    url(r'^ingresar/$', 'pacientes.views.ingresar', name="login"),
    url(r'^registro$', (RegistroPacientesView.as_view()),
        name='pacientesregistro'),
    url(r'^pacientes-registrados$', (PacientesRegistrados.as_view()),
        name='pacientesregistrados'),
    url(r'^estudios-default$', (EstudiosDefaultList.as_view()),
        name='estudiosdefault'),
    url(r'^estudios-registrados$', (EstudiosRegistrados.as_view()),
        name='estudiosregistrados'),
    url(r'^estudios_interpretacion$', (EstudiosInterpretacion.as_view()),
        name='estudiosinterpretacion'),
    url(r'^perfil/(?P<id>\d+)$', (PerfilPaciente.as_view()),
        name='perfilpaciente'),
    url(r'^crear_interpretacion/(?P<id>\d+)/(?P<est>\d+)', (
        CrearInterpretacion.as_view()), name='crearinterpretacion'),
    url(r'^detalle/(?P<id>\d+)$', (Detalle.as_view()),
        name='detalleinterpretacion'),
    url(r'^editar_paciente/(?P<id>\d+)$', (EditarPaciente.as_view()),
        name='editarpacientes'),
    url(r'^editar_intepretacion/(?P<id>\d+)$', (
        EditarInterpretacion.as_view()), name='editarinterpretacion'),
    url(r'^editar_intepretacion_default/(?P<id>\d+)$', (
        EditarInterpretacionDefault.as_view()),
        name='editarinterpretaciondefault'),
    url(r'^imprimir/(?P<id>\d+)$', (Imprimir.as_view()),
        name='imprimirinterpretacion'),
    url(r'^eliminar/(?P<id>\d+)$', 'pacientes.views.EliminarPaciente', name='deletepatient'),
    url(r'^eliminar_interpretacion/(?P<id>\d+)$', 'pacientes.views.EliminarInterpretacion',
        name='eliminarintepretacion'),
    url(r'^eliminar_default/(?P<id>\d+)$', 'pacientes.views.EliminarMachotes',
        name='eliminarmachotes'),
    url(r'^detalle/(?P<id>\d+)$', (Detalle.as_view()),
        name='detalleinterpretacion'),
    url(r'^imprimir_excel/(?P<id>\d+)$', (ImprimirExcel.as_view()),
        name='imprimirexcel'),
    url(r'^/enviar/interpretacion/(?P<id>\d+)$', 'pacientes.views.sendinterpretation',
        name='send-interpretacion'),
    url(r'^/all/enviar/interpretacion/(?P<patient_id>\d+)$', 'pacientes.views.sendinterpretationall',
        name='send-interpretacion-all'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


)
