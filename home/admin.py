from django.contrib import admin
from home.models import Pintura


# admin.site.register(Pintura)
@admin.register(Pintura)
class PinturaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_de_creacion")

    list_display_links = ("nombre",)

    search_fields = ("nombre", "autor")

    list_filter = ("fecha_de_creacion",)

    ordering = ("nombre", "autor", "fecha_de_creacion")

    readonly_fields = ("fecha_de_creacion",)
