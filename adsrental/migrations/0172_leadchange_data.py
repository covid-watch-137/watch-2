# Generated by Django 2.0.6 on 2018-07-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0171_lead_extra_photo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadchange',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
