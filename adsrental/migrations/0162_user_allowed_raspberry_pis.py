# Generated by Django 2.0.5 on 2018-06-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0161_ec2instance_browser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allowed_raspberry_pis',
            field=models.ManyToManyField(to='adsrental.RaspberryPi'),
        ),
    ]
