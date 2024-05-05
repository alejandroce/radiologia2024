# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_estudio', models.CharField(max_length=500)),
                ('categoria', models.CharField(max_length=200, null=True, blank=True)),
                ('interpretacion_default', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospitales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_hospital', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Interpretaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interpretacion_creada', models.TextField()),
                ('nombre_estudio', models.CharField(max_length=100)),
                ('crated_at_date', models.DateField(auto_now_add=True)),
                ('crated_at_time', models.TimeField(auto_now_add=True)),
                ('archivo_interpretacion_1', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
                ('archivo_interpretacion_2', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
                ('archivo_interpretacion_3', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
                ('archivo_interpretacion_4', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
                ('archivo_interpretacion_5', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('especialidad', models.CharField(max_length=100, null=True, blank=True)),
                ('cedula', models.CharField(max_length=100, null=True, blank=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10, choices=[(b'Femenino', b'Femenino'), (b'Masculino', b'Masculino')])),
                ('edad', models.CharField(max_length=20, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('contacto_nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('contacto_telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('hospital', models.CharField(max_length=50, choices=[(b'CENTRO', b'Centro Medico Excel'), (b'IMSS', b'IMSS NO.1'), (b'PRADO', b'Centro Medico Del Prado'), (b'NUCLEO', b'Nucleo Radiologico'), (b'PERSONAL', b'Dr.David Aguilar Obeso'), (b'ECO', b'Ecodiagnostica Portatil Del Rio'), (b'INT', b'Instituto Nefrologico De Tijuana'), (b'GUADALAJARA', b'Hospital Guadalajara'), (b'CEMIQ', b'CEMIQ'), (b'CRUZ ROJA', b'Cruz Roja')])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('numero_seguro', models.CharField(max_length=30, null=True, blank=True)),
                ('medico_referencia', models.CharField(max_length=100, null=True, blank=True)),
                ('estudio_adicional', models.BooleanField(default=False)),
                ('fecha_elaboracion_estudio', models.DateField(null=True, blank=True)),
                ('hora_elaboracion_estudio', models.TimeField(null=True, blank=True)),
                ('estudio_1', models.ForeignKey(related_name='estudio1', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_10', models.ForeignKey(related_name='estudio10', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_2', models.ForeignKey(related_name='estudio2', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_3', models.ForeignKey(related_name='estudio3', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_4', models.ForeignKey(related_name='estudio4', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_5', models.ForeignKey(related_name='estudio5', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_6', models.ForeignKey(related_name='estudio6', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_7', models.ForeignKey(related_name='estudio7', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_8', models.ForeignKey(related_name='estudio8', blank=True, to='pacientes.Estudios', null=True)),
                ('estudio_9', models.ForeignKey(related_name='estudio9', blank=True, to='pacientes.Estudios', null=True)),
                ('estudios', models.ManyToManyField(to='pacientes.Estudios')),
            ],
        ),
        migrations.CreateModel(
            name='UserHospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.ForeignKey(blank=True, to='pacientes.Hospitales', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='interpretaciones',
            name='id_paciente',
            field=models.ForeignKey(blank=True, to='pacientes.Paciente', null=True),
        ),
    ]
