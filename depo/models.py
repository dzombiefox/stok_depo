from __future__ import unicode_literals
from django.db import models



#Create your models here.
class Depo(models.Model):
    kodeDepo = models.CharField(max_length=15,verbose_name="Kode Depo")
    namaDepo = models.CharField(max_length=25,verbose_name="Nama Depo")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.namaDepo
