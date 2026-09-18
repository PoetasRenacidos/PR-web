#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.contrib import admin
from apps.users.models import UsuarioTallerista, UsuarioBase
from django.forms import PasswordInput

admin.site.register(UsuarioBase)
admin.site.register(UsuarioTallerista)

@admin.register(UsuarioBase)
class UsuarioBaseAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'password' in form.base_fields:
            form.base_fields['password'].widget = PasswordInput(render_value=True)
        return form


@admin.register(UsuarioTallerista)
class UsuarioTallerista(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'password' in form.base_fields:
            form.base_fields['password'].widget = PasswordInput(render_value=True)
        return form
