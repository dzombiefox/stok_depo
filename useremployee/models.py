# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from employee .models import Karyawan
# Create your models here.

class UserEmployee(models.Model):
    user=models.OneToOneField(User)
    karyawan=models.ForeignKey(Karyawan,verbose_name="Employee")
    def __str__(self):
        return self.karyawan.namaKaryawan