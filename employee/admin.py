# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Karyawan
class KaryawanAdmin(admin.ModelAdmin):
    class meta:
        model = Karyawan
    list_display = ['__str__']

admin.site.register(Karyawan,KaryawanAdmin)
