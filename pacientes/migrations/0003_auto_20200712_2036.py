# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_archivosinterpretacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estudios',
            field=models.ManyToManyField(to='pacientes.Estudios', null=True, blank=True),
        ),
    ]
