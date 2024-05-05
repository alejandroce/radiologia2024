# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivosInterpretacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(null=True, upload_to=b'Documentos/imagen', blank=True)),
                ('interpretacion', models.ForeignKey(to='pacientes.Interpretaciones')),
            ],
        ),
    ]
