# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-24 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0038_ec2instance_raspberry_pi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ec2instance',
            name='password',
            field=models.CharField(default=b'AdsInc18', max_length=255),
        ),
    ]
