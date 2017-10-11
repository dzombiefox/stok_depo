# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from depo .models import Depo
# Create your models here.
class Karyawan(models.Model):
    namaKaryawan=models.CharField(max_length=50)
    depo=models.ForeignKey(Depo)
    prof_pic = models.ImageField("Photo Profile", upload_to='prof_pic/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.namaKaryawan