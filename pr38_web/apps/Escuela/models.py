#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from apps.users.models import UsuarioTallerista, UsuarioBase

ARTES_CHOICES = [
    ('arquitectura',    'Arquitectura'),
    ('escultura',       'Escultura'),
    ('pintura',         'Pintura'),
    ('musica',          'Música'),
    ('literatura',      'Literatura / Poesía'),
    ('danza',           'Danza'),
    ('teatro',          'Teatro'),
    ('cine',            'Cine / Audiovisual'),
]

class Taller(models.Model):
    nombre = models.CharField(max_length=254, verbose_name="Nombre del taller")
    tipo_taller = models.CharField(choices=ARTES_CHOICES, max_length=30, verbose_name="Área relacionada")
    fk_tallerista = models.ForeignKey(
        UsuarioTallerista,
        to_field='email',
        on_delete=models.CASCADE,
        verbose_name="email tallerista (VERIFICA)"
    )
    fecha = models.DateField(editable=True, verbose_name="Fecha")
    hora = models.TimeField(editable=True, verbose_name="Hora")
    duracion = models.PositiveSmallIntegerField(verbose_name="duración (horas)")
    lugar = models.CharField(blank=True, null=True, max_length=254, verbose_name="Dirección del taller")
    valor = models.IntegerField(blank=True, null=True, verbose_name="Valor de entrada (si aplica)")
    aforo_max = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Aforo máximo")

class usuario_por_taller(models.Model): # Modelo intermedio entre USUARIO y TALLER.
    fk_UsuarioBase = models.ForeignKey(UsuarioBase, on_delete=models.CASCADE)
    fk_Taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint( # evita pares duplicados entre fk_UsuarioBase y fk_Taller
                fields=["fk_UsuarioBase", "fk_Taller"],
                name="unique_usuario_taller"
            )
        ]