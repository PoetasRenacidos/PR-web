#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Las 8 artes clásicas/contemporáneas para el perfil del usuario/tallerista
# Campo de tipo CHOICE para que el usuario seleccione una única opción.
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

class NormalUser(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, db_index=True, verbose_name="Correo electrónico")
    phone_number = models.BigIntegerField(blank=True, null=True, max_length=20, verbose_name="Teléfono")
    password = models.CharField(max_length=128, default="0000", verbose_name="Contraseña")
    fav_art = models.CharField(max_length=30, choices=ARTES_CHOICES, verbose_name="Arte favorito")
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name="Ciudad de residencia")

class TeacherUser(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, db_index=True, verbose_name="Correo electrónico")
    phone_number = models.BigIntegerField(blank=True, null=True, max_length=20, verbose_name="Teléfono")
    password = models.CharField(max_length=128, default="", verbose_name="Contraseña")
    profession = models.CharField(max_length=60, choices=ARTES_CHOICES, verbose_name="Rubro/Profesión")
    years_experience = models.IntegerField(verbose_name="Años de experiencia")
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name="Ciudad de residencia")

class user_per_teacher(models.Model): # Intermediate table to mantain DDBB standards
    fk_NormalUser = models.ForeignKey(NormalUser, on_delete=models.CASCADE, verbose_name="Usuario normal")
    fk_TeacherUser = models.ForeignKey(TeacherUser, on_delete=models.CASCADE, verbose_name="Profesor")

    class Meta:
        constraints = [
            models.UniqueConstraint( # Avoid duplicate pairs between fk_NormalUser & fk_TeacherUser
                fields=["fk_NormalUser", "fk_TeacherUser"],
                name="unique_user_teacher"
            )
        ]