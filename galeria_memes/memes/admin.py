"""
Modelo + Admin: registra Meme en Django Admin para tener el CRUD "gratis".
"""
from django.contrib import admin

from .models import Meme


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "autor", "publicado", "creado")
    list_filter = ("categoria", "publicado", "autor")
    search_fields = ("titulo", "descripcion")
