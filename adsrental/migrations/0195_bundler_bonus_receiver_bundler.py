# Generated by Django 2.1 on 2018-09-03 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0194_auto_20180828_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundler',
            name='bonus_receiver_bundler',
            field=models.ForeignKey(blank=True, help_text='Bundler that receives weekly bonuses for qualified leads.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_donor', to='adsrental.Bundler'),
        ),
    ]
