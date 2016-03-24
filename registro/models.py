# -*- coding: 850 -*-
### Codificacion para usar ¤


from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.
## Sector Model
class Sector(models.Model):
    name = models.CharField('Nombre del Sector',max_length=100, unique=True)
    timestamp =  models.DateTimeField(default = datetime.now)
#    updated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sectores'

## Evento
class Evento(models.Model):
    name = models.CharField('Nombre del Evento',max_length=50, unique=True)
    event_date= models.DateField('Fecha del evento')
    timestamp =  models.DateTimeField(default = datetime.now)
##    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Eventos"

## Persona Model
class Persona(models.Model):
    name = models.CharField('Asistente',max_length=50)
    email = models.EmailField('Facebook Email',unique=True)
    phone_number = PhoneNumberField('Celular +503 XXXXXXX', unique=True)
    birth_date = models.DateField('Fecha de Nacimiento')
    sector = models.ForeignKey(Sector, verbose_name = u'Asiste al Sector')
    timestamp =  models.DateTimeField(default = datetime.now)
##    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name

    def __getattr__(self, item):
        return self.item

## Asistencia Evento
## Sector Model
class Asistencia(models.Model):
    persona = models.ForeignKey(Persona, verbose_name = u'Persona que Asiste')
    evento = models.ForeignKey(Evento, verbose_name = u'Evento')
    timestamp =  models.DateTimeField(default = datetime.now)
##    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
       return str(self.persona.name)+"-"+str(self.evento.name)

    class Meta:
        verbose_name_plural = 'Jovenes que Asisten los Eventos'
        verbose_name = "Joven Asistencia"
        unique_together = ('persona', 'evento')