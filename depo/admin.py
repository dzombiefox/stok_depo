# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Depo
class DepoAdmin(admin.ModelAdmin):
    class meta:
        model = Depo
    list_display = ('kodeDepo','namaDepo')

admin.site.register(Depo,DepoAdmin)
