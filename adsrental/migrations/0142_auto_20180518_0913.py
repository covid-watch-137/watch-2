# Generated by Django 2.0.3 on 2018-05-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0141_ec2instance_instance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ec2instance',
            name='instance_type',
            field=models.CharField(default='t2.medium', help_text='Size of AWS EC2', max_length=50),
        ),
    ]
