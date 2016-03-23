# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 16:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20160319_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='evento',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='persona',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]