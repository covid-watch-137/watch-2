# Generated by Django 2.1 on 2018-09-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0198_auto_20180909_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='tested',
        ),
    ]