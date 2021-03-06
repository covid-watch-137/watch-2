# Generated by Django 2.1.5 on 2019-02-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0228_bundlerpayment_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundlerpayment',
            name='payment_type',
            field=models.CharField(choices=[('account', 'Lead account activated'), ('account_parent', "Child's Lead account activated"), ('account_second_parent', "Child's Lead account activated (2nd parent)"), ('bonus', 'Bonus'), ('chargeback', 'Chargeback')], db_index=True, default='account', max_length=50),
        ),
    ]
