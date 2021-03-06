# Generated by Django 2.0.5 on 2018-06-05 00:23

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0149_auto_20180531_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundler',
            name='facebook_chargeback',
            field=models.DecimalField(decimal_places=2, default=Decimal('50'), help_text='Chargeback value for Facebook accounts.', max_digits=8),
        ),
        migrations.AddField(
            model_name='bundler',
            name='google_changeback',
            field=models.DecimalField(decimal_places=2, default=Decimal('50'), help_text='Chargeback value for Google accounts.', max_digits=8),
        ),
    ]
