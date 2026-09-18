#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.contrib import admin
from apps.Escuela.models import Taller, usuario_por_taller

admin.site.register(Taller)
admin.site.register(usuario_por_taller)
