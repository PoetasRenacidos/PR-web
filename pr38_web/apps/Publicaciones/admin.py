#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.contrib import admin
from apps.Publicaciones.models import ObraLiteraria, Post

admin.site.register(ObraLiteraria)
admin.site.register(Post)
