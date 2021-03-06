# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-06 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0007_auto_20171206_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberrypi',
            name='first_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='raspberrypi',
            name='ipaddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='raspberrypi',
            name='last_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
