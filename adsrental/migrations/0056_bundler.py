# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-04 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0055_auto_20180204_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('utm_source', models.CharField(db_index=True, max_length=255)),
                ('adsdb_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
