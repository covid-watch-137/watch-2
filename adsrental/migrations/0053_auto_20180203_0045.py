# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-03 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0052_auto_20180203_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.CharField(default='[Empty]', max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='country',
            field=models.CharField(blank=True, default='United States', max_length=50, null=True),
        ),
    ]
