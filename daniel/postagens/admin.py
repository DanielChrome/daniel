# -*- coding: utf8 -*-
from django.contrib import admin
from daniel.postagens.models import Postagem, Categoria


admin.site.register(Postagem)
admin.site.register(Categoria)
