# Generated by Django 2.0.3 on 2018-04-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0128_bundlerpaymentsreport_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadaccount',
            name='sync_with_adsdb',
            field=models.BooleanField(default=False),
        ),
    ]