# -*- coding: utf8 -*-
from django.contrib import admin
from daniel.postagens.models import Postagem, Categoria, Pagina

class Posts(admin.ModelAdmin):
	fields = ['titulo','categoria','paginas','usuario','conteudo','datapublicacao','imagem']
	list_display = ('titulo','datapublicacao','categoria')
	list_filter = ['datapublicacao']
	search_fields = ['titulo']
	date_hierarchy = 'datapublicacao'
admin.site.register(Postagem,Posts)
admin.site.register(Categoria)
admin.site.register(Pagina)
