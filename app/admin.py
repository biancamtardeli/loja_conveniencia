from django.contrib import admin
from .models import *
from django.utils.html import format_html

admin.site.register(Categoria)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'imagem_display')

    def imagem_display(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.imagem.url)
        return "Sem imagem"
    imagem_display.short_description = 'Imagem'

# Registrando o modelo no admin
admin.site.register(Produto, ProdutoAdmin)
