# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Size
class SizeAdmin(admin.ModelAdmin):
    class meta:
        model = Size
    list_display = ['__str__']

admin.site.register(Size,SizeAdmin)
