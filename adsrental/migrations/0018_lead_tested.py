# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-19 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0017_auto_20171214_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='tested',
            field=models.BooleanField(default=False),
        ),
    ]
