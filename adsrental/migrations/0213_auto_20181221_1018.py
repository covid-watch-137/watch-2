# Generated by Django 2.1.3 on 2018-12-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0212_auto_20181208_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundlerleadstat',
            name='delivered_last_14_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bundlerleadstat',
            name='delivered_not_connected_last_14_days',
            field=models.IntegerField(default=0),
        ),
    ]
