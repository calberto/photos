# admin.py
from django.contrib import admin
from core.models import Cidade, Fotografia

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'pais', 'total_fotos']
    list_filter = ['estado', 'pais']
    search_fields = ['nome', 'estado']
    ordering = ['nome']
    
    def total_fotos(self, obj):
        return obj.fotografias.count()
    total_fotos.short_description = 'Total de Fotos'

@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cidade', 'data_upload', 'ativa']
    list_filter = ['cidade', 'ativa', 'data_upload']
    search_fields = ['titulo', 'descricao', 'cidade__nome']
    list_editable = ['ativa']
    ordering = ['-data_upload']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'cidade')
        }),
        ('Imagem', {
            'fields': ('imagem',)
        }),
        ('Configurações', {
            'fields': ('ativa',)
        }),
    )