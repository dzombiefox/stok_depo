# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0004_stok_depo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StokPabrik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('barang', models.TextField(max_length=100)),
                ('stok', models.IntegerField()),
            ],
        ),
    ]