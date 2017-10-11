# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Brand
class BrandAdmin(admin.ModelAdmin):
    class meta:
        model = Brand
    list_display = ['__str__']
admin.site.register(Brand,BrandAdmin)
