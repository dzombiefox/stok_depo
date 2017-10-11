from __future__ import unicode_literals
from django.db import models



#Create your models here.
class Size(models.Model):
    namaUkuran= models.CharField(max_length=15,verbose_name="Nama Ukuran")
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)

    def __str__(self):
        return  self.namaUkuran
