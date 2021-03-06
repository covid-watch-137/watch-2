# Generated by Django 2.0.3 on 2018-03-26 13:04

import adsrental.models.mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0095_lead_tracking_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Banned', 'Banned')], max_length=50)),
                ('account_type', models.CharField(choices=[('Facebook', 'Facebook'), ('Google', 'Google')], max_length=50)),
                ('friends', models.BigIntegerField(default=0)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('wrong_password_date', models.DateTimeField(blank=True, help_text='Date when password was reported as wrong.', null=True)),
                ('bundler_paid', models.BooleanField(default=False, help_text='Is revenue paid to bundler.')),
                ('adsdb_account_id', models.CharField(blank=True, help_text='Corresponding Account ID in Adsdb database. used for syncing between databases.', max_length=255, null=True)),
                ('active', models.BooleanField(default=False, help_text='If false, entry considered as deleted')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            bases=(models.Model, adsrental.models.mixins.FulltextSearchMixin),
        ),
        migrations.AlterField(
            model_name='ec2instance',
            name='lead',
            field=models.OneToOneField(blank=True, help_text='Corresponding lead', null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsrental.Lead'),
        ),
        migrations.AlterField(
            model_name='ec2instance',
            name='version',
            field=models.CharField(default='2.7.2', help_text='AWS EC2 Firmware version', max_length=255),
        ),
        migrations.AlterField(
            model_name='lead',
            name='bundler',
            field=models.ForeignKey(blank=True, default=None, help_text='New UTM source representation', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adsrental.Bundler'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='photo_id',
            field=models.FileField(blank=True, help_text='Photo uploaded by user on registration.', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lead',
            name='raspberry_pi',
            field=models.OneToOneField(blank=True, default=None, help_text='Linked RaspberryPi device', null=True, on_delete=django.db.models.deletion.SET_NULL, to='adsrental.RaspberryPi'),
        ),
        migrations.AlterField(
            model_name='leadchange',
            name='edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='utm_source',
            field=models.CharField(blank=True, default='', help_text='If not NULL, leads in dashboard will be filtered by this utm_source. SHould be changed to bundler.', max_length=255),
        ),
        migrations.AddField(
            model_name='leadaccount',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adsrental.Lead'),
        ),
    ]
