# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unclesback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
