#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from apps.users.models import UsuarioBase

GENEROS_LITERARIOS_CHOICES = [
    ('aventura', 'Aventura'),
    ('autobiografia', 'Autobiografía'),
    ('biografia', 'Biografía'),
    ('ciencia_ficcion', 'Ciencia ficción'),
    ('cuento', 'Cuento'),
    ('cronica', 'Crónica'),
    ('distopia', 'Distopía'),
    ('ensayo', 'Ensayo'),
    ('eutherpoiesis', 'Eutherpoiésis'),
    ('experimental', 'Literatura experimental'),
    ('literatura_infantil', 'Literatura infantil'),
    ('literatura_juvenil', 'Literatura juvenil'),
    ('fantasia', 'Fantasía'),
    ('folclor', 'Folclor'),
    ('historica', 'Novela histórica'),
    ('humor', 'Humor'),
    ('mitologia', 'Mitología'),
    ('misterio', 'Misterio/Suspenso'),
    ('novela', 'Novela'),
    ('poesia', 'Poesía'),
    ('realismo_magico', 'Realismo mágico'),
    ('romance', 'Romance'),
    ('satira', 'Sátira'),
    ('teatro', 'Teatro'),
    ('terror', 'Terror'),
]

class ObraLiteraria(models.Model):
    titulo = models.CharField(max_length=254, verbose_name="Título de la obra", db_index=True)
    autor = models.ForeignKey(
        UsuarioBase,
        to_field='nick_name',
        on_delete=models.CASCADE,
        verbose_name="Autor/a de la obra"
    )
    corriente = models.CharField(max_length=30, choices=GENEROS_LITERARIOS_CHOICES, verbose_name="Género literario")
    sinopsis = models.CharField(max_length=254, verbose_name="Sinópsis")
    fecha_publicacion = models.DateField(verbose_name="Fecha de publicación")


class Post(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    autor = models.ForeignKey(
            UsuarioBase,
            to_field='nick_name',
            on_delete=models.CASCADE,
            verbose_name="Autor/a del post"
        )
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='Posts/', null=True, blank=True, verbose_name="Imágen")
    video = models.FileField(upload_to='Posts/', null=True, blank=True, verbose_name="Video")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    activo = models.BooleanField(default=True, verbose_name="Estado (default: activo)")