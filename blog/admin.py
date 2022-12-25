from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','deskripsi','tahun_lahir','tahun_wafat','tahun_kenaikan')

admin.site.register(Artikel, ArtikelAdmin)