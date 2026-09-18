#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.contrib import admin
from apps.users.models import UsuarioTallerista, UsuarioBase

admin.site.register(UsuarioBase)
admin.site.register(UsuarioTallerista)
