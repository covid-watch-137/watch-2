# Generated by Django 2.1.5 on 2019-02-18 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0230_auto_20190217_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundlerpayment',
            name='extra',
            field=models.TextField(blank=True, null=True),
        ),
    ]