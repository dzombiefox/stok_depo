# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0002_auto_20170907_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sk_box', models.CharField(max_length=12)),
                ('sk_persen', models.CharField(max_length=12)),
                ('sp_box', models.CharField(max_length=12)),
                ('sp_persen', models.CharField(max_length=12)),
                ('sh_box', models.CharField(max_length=12)),
                ('sh_persen', models.CharField(max_length=12)),
                ('sa_box', models.CharField(max_length=12)),
                ('sa_persen', models.CharField(max_length=12)),
                ('s_boxph', models.CharField(max_length=12)),
                ('s_persenph', models.CharField(max_length=12)),
                ('s_totalbox', models.CharField(max_length=12)),
                ('s_totalpersen', models.CharField(max_length=12)),
            ],
        ),
    ]