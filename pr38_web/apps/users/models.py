#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.hashers import make_password

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

class UsuarioBase(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre completo")
    nick_name = models.CharField(unique=True, max_length=40)
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    fav_art = models.CharField(max_length=30, choices=ARTES_CHOICES, verbose_name="Arte favorito")
    phone_number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Teléfono")
    organization = models.CharField(max_length=254,blank=True,null=True,verbose_name="Organización (si aplica)")
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name="Ciudad de residencia")
    password = models.CharField(max_length=128, verbose_name="Contraseña")

    def save(self, *args, **kwargs): # Encriptación automática de 'password'
        if self.password and not self.password.startswith('pbkdf2_'): # la encripta si no lo está
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class UsuarioTallerista(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre completo")
    nick_name = models.CharField(unique=True, max_length=40)
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Teléfono")
    password = models.CharField(max_length=128, default="", verbose_name="Contraseña")
    profession = models.CharField(max_length=60, choices=ARTES_CHOICES, verbose_name="Rubro/Profesión")
    years_experience = models.PositiveSmallIntegerField(verbose_name="Años de experiencia")
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name="Ciudad de residencia")
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs): # Encriptación automática de 'password'
        if self.password and not self.password.startswith('pbkdf2_'): # la encripta si no lo está
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
