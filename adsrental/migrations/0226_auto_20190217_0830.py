# Generated by Django 2.1.5 on 2019-02-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0225_auto_20190217_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundlerpayment',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsrental.BundlerPaymentsReport'),
        ),
    ]
