# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-21 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0031_remove_raspberrypi_update_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberrypi',
            name='version',
            field=models.CharField(default='1.0.0', max_length=20),
        ),
    ]
