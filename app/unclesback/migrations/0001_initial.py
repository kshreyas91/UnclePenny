# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
     
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=12)),
                ('banknumber', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=25)),
                ('bankname', models.CharField(max_length=100)),
            ],
        ),
    ]
