# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-10 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0007_auto_20171010_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stokpabrik',
            name='stok',
            field=models.CharField(max_length=15),
        ),
    ]
