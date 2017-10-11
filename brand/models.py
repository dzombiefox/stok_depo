from __future__ import unicode_literals
from django.db import models



#Create your models here.
class Brand(models.Model):
    namaBrand = models.CharField(max_length=15,verbose_name="Merk")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.namaBrand