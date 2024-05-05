from django.contrib.auth.models import User
from django.db import models
from radiologia.listas import genero
from utils.emails import send_simple_email


class Hospitales(models.Model):
    nombre_hospital = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        db_table = 'hospitales'

class Estudios(models.Model):
    nombre_estudio = models.CharField(max_length=500, null=False, blank=False)
    categoria = models.CharField(max_length=200, null=True, blank=True)
    interpretacion_default = models.TextField(
        null=False, blank=False)

    def __unicode__(self):
        return self.nombre_estudio

    class Meta:
        db_table = 'estudios'


class Paciente(models.Model):
    CENTRO = 1
    IMSS = 2
    PRADO = 3
    PERSONAL = 4
    NUCLEO = 5
    hospitales =(
                ('CENTRO', 'Centro Medico Excel'),
                ('IMSS', 'IMSS NO.1'),
                ('PRADO', 'Centro Medico Del Prado'),
                ('NUCLEO', 'Nucleo Radiologico'),
                ('PERSONAL', 'Dr.David Aguilar Obeso'),
                ('ECO', 'Ecodiagnostica Portatil Del Rio'),
                ('INT', 'Instituto Nefrologico De Tijuana'),
                ('GUADALAJARA', 'Hospital Guadalajara'),
                ('CEMIQ', 'CEMIQ'),
                ('CRUZ ROJA', 'Cruz Roja'),
                ('AGEcography" Diagnostico Medico', 'AGEcography" Diagnostico Medico'),
                ('PREMIER Centro Medico', 'PREMIER Centro Medico'),
                ('SIMSA', 'SIMSA'))
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=30, null=False, blank=False)
    apellido_materno = models.CharField(max_length=30, null=False, blank=False)
    sexo = models.CharField(max_length=10, null=False, blank=False, choices=genero)
    edad = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    contacto_nombre = models.CharField(max_length=100, null=True, blank=True)
    contacto_telefono = models.CharField(max_length=20, null=True, blank=True)
    hospital = models.CharField(choices=hospitales, max_length=50, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    numero_seguro = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    estudio_1 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio1')
    estudio_2 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio2')
    estudio_3 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio3')
    estudio_4 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio4')
    estudio_5 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio5')
    estudio_6 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio6')
    estudio_7 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio7')
    estudio_8 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio8')
    estudio_9 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio9')
    estudio_10 = models.ForeignKey(Estudios, null=True, blank=True, related_name='estudio10')
    medico_referencia = models.CharField(null=True, blank=True, max_length=100)
    estudio_adicional = models.BooleanField(default=False)
    fecha_elaboracion_estudio = models.DateField(null=True, blank=True)
    hora_elaboracion_estudio = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'paciente'


class SolicitudDeEstudios(models.Model):
    paciente = models.ForeignKey(Paciente)
    medico_referencia = models.CharField(null=True, blank=True, max_length=100)
    estudio_adicional = models.BooleanField(default=False)
    fecha_elaboracion_estudio = models.DateField(null=True, blank=True)
    hora_elaboracion_estudio = models.TimeField(null=True, blank=True)
    hospital = models.ForeignKey(Hospitales)

    class Meta:
        db_table = 'solicitud'


class ArchivosInterpretacion(models.Model):
    archivo = models.FileField(upload_to="Documentos/imagen", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'archivos_interpretacion'


class Interpretaciones(models.Model):
    id_paciente = models.ForeignKey(Paciente, null=True, blank=True)
    solicitud = models.ForeignKey(SolicitudDeEstudios, null=True, blank=True)
    interpretacion_creada = models.TextField()
    nombre_estudio = models.CharField(max_length=100, null=False, blank=False)
    crated_at_date = models.DateField(auto_now_add=True)
    crated_at_time = models.TimeField(auto_now_add=True)
    archivos = models.ManyToManyField(ArchivosInterpretacion, null=True)

    class Meta:
        db_table = 'interpretacion'


class ArchivoPDFInterpretacion(models.Model):
    nombre_archivo = models.CharField(null=True, max_length=900)
    interpretacion = models.ForeignKey(Interpretaciones)

    class Meta:
        db_table = 'archivo_pdf_interpretacion'


class Medico(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    cedula = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        db_table = 'medico'


class UserHospital(models.Model):
    hospital = models.ForeignKey(Hospitales, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        db_table = 'user_hospital'
