# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import unclesback.listField


class Migration(migrations.Migration):

    dependencies = [
        ('unclesback', '0002_statusobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('members', unclesback.listField.ListField()),
                ('challenge_name', models.CharField(max_length=200)),
                ('status', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='currentsavings',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='futureestimate',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
    ]
