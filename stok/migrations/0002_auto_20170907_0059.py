# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stok',
            old_name='jumlah',
            new_name='a_box',
        ),
        migrations.RemoveField(
            model_name='stok',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='stok',
            name='persen',
        ),
        migrations.AddField(
            model_name='stok',
            name='a_persen',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='h_box',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='h_persen',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='k_box',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='k_persen',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='p_box',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stok',
            name='p_persen',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]