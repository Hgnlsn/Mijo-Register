# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Evento')),
                ('event_date', models.DateField(verbose_name='Fecha del evento')),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'verbose_name_plural': 'Sectores'},
        ),
        migrations.AlterField(
            model_name='persona',
            name='birth_date',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Facebook Email'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Asistente'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Celular +503 XXXXXXX'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Sector', verbose_name='Asiste al Sector'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre del Sector'),
        ),
    ]
