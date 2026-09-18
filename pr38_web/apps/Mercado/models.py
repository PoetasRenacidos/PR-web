#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from apps.users.models import UsuarioBase

CATEGORIAS_PRODUCTO = [
    ('artesanias', 'Artesanías'),
    ('literatura', 'Literatura'),
    ('vestuario', 'Vestuario'),
    ('audiovisual', 'Audiovisuales'),
    ('fotografia', 'Fotografía'),
    ('patrimonio', 'Patrimonio y cultura'),
    ('alimentos', 'Bebidas/Alimentación'),
    ('otros', 'Otros'),
]

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=254, verbose_name="Nombre del artículo")
    fk_usuario = models.ForeignKey(
        UsuarioBase,
        to_field='email',
        on_delete=models.CASCADE,
        verbose_name="email (VERIFICA)"
    )
    precio = models.PositiveIntegerField(verbose_name="Precio del producto")
    descripcion = models.TextField(verbose_name="Descripción del producto")
    categoria = models.CharField(choices=CATEGORIAS_PRODUCTO, max_length=25, verbose_name="Categoría")
    imagen = models.ImageField(upload_to='Productos/')
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad de origen")
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

