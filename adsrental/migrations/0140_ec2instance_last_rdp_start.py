# Generated by Django 2.0.3 on 2018-05-15 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0139_bundlerpaymentsreport_email_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='ec2instance',
            name='last_rdp_start',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Last time when RDP connect page was accessed for this instance'),
        ),
    ]