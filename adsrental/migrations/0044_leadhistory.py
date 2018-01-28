# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-28 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0043_auto_20180125_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('checks_offline', models.IntegerField(default=0)),
                ('checks_online', models.IntegerField(default=0)),
                ('checks_wrong_password', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adsrental.Lead')),
            ],
        ),
    ]
