# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0088_auto_20180309_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ec2instance',
            name='ssh_up',
        ),
        migrations.RemoveField(
            model_name='ec2instance',
            name='tunnel_up',
        ),
    ]
