# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-14 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0016_auto_20171214_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberrypi',
            name='last_seen',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
