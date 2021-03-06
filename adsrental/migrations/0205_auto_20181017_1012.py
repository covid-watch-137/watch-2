# Generated by Django 2.1 on 2018-10-17 17:12

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0204_lead_isp'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundler',
            name='facebook_screenshot_chargeback',
            field=models.DecimalField(decimal_places=2, default=Decimal('50'), help_text='Chargeback value for Facebook Screenshot accounts.', max_digits=8),
        ),
        migrations.AddField(
            model_name='bundler',
            name='facebook_screenshot_parent_payment',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Amount to withdraw from lead payment to be paid to parent bundler.', max_digits=8),
        ),
        migrations.AddField(
            model_name='bundler',
            name='facebook_screenshot_payment',
            field=models.DecimalField(decimal_places=2, default=Decimal('125'), help_text='Payout for Facebook Screenshot accounts', max_digits=8),
        ),
        migrations.AddField(
            model_name='bundler',
            name='facebook_screenshot_second_parent_payment',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Amount to withdraw from lead payment to be paid to parent bundler.', max_digits=8),
        ),
        migrations.AlterField(
            model_name='bundler',
            name='facebook_payment',
            field=models.DecimalField(decimal_places=2, default=Decimal('125'), help_text='Payout for Facebook accounts', max_digits=8),
        ),
        migrations.AlterField(
            model_name='bundler',
            name='google_payment',
            field=models.DecimalField(decimal_places=2, default=Decimal('125'), help_text='Payout for Google accounts', max_digits=8),
        ),
    ]
