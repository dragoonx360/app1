# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('modelo', models.CharField(max_length=50)),
                ('fecha_lanzamiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('fabricante', models.CharField(max_length=200)),
                ('versionOS', models.CharField(max_length=5)),
            ],
        ),
    ]
