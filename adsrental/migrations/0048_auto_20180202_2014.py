# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-02 20:14
from __future__ import unicode_literals

from django.db import migrations, models
from adsrental.forms import SignupForm


def populate_addresses(apps, schema_editor):
    Lead = apps.get_model('adsrental', 'Lead')
    for lead in Lead.objects.all():
        address = lead.address
        lead.country = address.split(',')[-1].strip()
        address = ','.join(address.split(',')[:-1])
        lead.postal_code = address.split(',')[-1].strip()
        address = ','.join(address.split(',')[:-1])
        lead.state = address.split(',')[-1].strip()
        if lead.state in dict(SignupForm.STATE_CHOICES).keys():
            address = ','.join(address.split(',')[:-1])
            lead.city = address.split(',')[-1].strip()
        else:
            lead.city = lead.state
            lead.state = ''
        address = ','.join(address.split(',')[:-1])
        lead.street = address.strip()
        lead.save()


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0047_auto_20180201_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='fb_friends',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lead',
            name='fb_profile_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RunPython(populate_addresses, reverse_code=migrations.RunPython.noop),
    ]
