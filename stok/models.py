# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from size .models import Size
from brand .models import Brand
from django.contrib.auth.models import User
from depo .models import Depo
# Create your models here.
class Stok(models.Model):
    tanggal = models.DateField()
    size = models.ForeignKey(Size)
    kita = models.CharField(max_length=12)
    picasso = models.CharField(max_length=12)
    harmony = models.CharField(max_length=12)
    atena = models.CharField(max_length=12)
    # k_box = models.CharField(max_length=12)
    # k_persen =models.CharField(max_length=12)
    # p_box = models.CharField(max_length=12)
    # p_persen = models.CharField(max_length=12)
    # h_box = models.CharField(max_length=12)
    # h_persen = models.CharField(max_length=12)
    # a_box = models.CharField(max_length=12)
    # a_persen = models.CharField(max_length=12)
    user = models.ForeignKey(User)
    depo = models.ForeignKey(Depo)


    # persen=models.CharField(max_length=25)
    # jumlah = models.CharField(max_length=12)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # def __str__(self):
    #     return  self.size

    # def box_plus(self):
    #     return int(self.p_box)+int(self.h_box)
    #
    # def persen_plus(self):
    #     return float(self.p_persen)+float(self.h_persen)
    #
    # def sum_box(self):
    #     return int(self.k_box)+int(self.p_box)+int(self.h_box)+int(self.a_box)
    #
    # def sum_persen(self):
    #     return  float(self.k_persen) + float(self.p_persen) + float(self.h_persen) + float (self.a_persen)


class Standard(models.Model):
    sk_box = models.CharField(max_length=12)
    sk_persen = models.CharField(max_length=12)
    sp_box = models.CharField(max_length=12)
    sp_persen = models.CharField(max_length=12)
    sh_box = models.CharField(max_length=12)
    sh_persen = models.CharField(max_length=12)
    sa_box = models.CharField(max_length=12)
    sa_persen = models.CharField(max_length=12)
    s_boxph = models.CharField(max_length=12)
    s_persenph = models.CharField(max_length=12)
    s_totalbox = models.CharField(max_length=12)
    s_totalpersen = models.CharField(max_length=12)


class StokPabrik(models.Model):
    tanggal = models.DateField()
    barang = models.TextField(max_length=100)
    stok =models.FloatField()