# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-02 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0049_lead_sf_leadid'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]