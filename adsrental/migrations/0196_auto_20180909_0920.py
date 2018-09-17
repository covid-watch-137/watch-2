# Generated by Django 2.1 on 2018-09-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0195_bundler_bonus_receiver_bundler'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberrypi',
            name='proxy_hostname',
            field=models.CharField(default='178.128.1.68', help_text='Hostname tunnel to proxykeeper', max_length=50),
        ),
        migrations.AddField(
            model_name='raspberrypi',
            name='proxy_password',
            field=models.CharField(default='keepitsecret', help_text='Hostname password for proxykeeper user', max_length=50),
        ),
    ]