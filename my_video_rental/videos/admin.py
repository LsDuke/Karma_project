from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
#change l'ordre des champs dans la console admin
    fields=['release_year','title','length']

#rajoute un champs de recherche
    search_fields = ['title','length']

    list_filter = ['release_year','length','title']

    list_display = ['title','release_year','length']
#besoin d'un list_display pour un list_editable
    list_editable = ['length']

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
