# Generated by Django 2.1.7 on 2019-07-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0250_auto_20190712_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='comments_cache',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leadaccount',
            name='comments_cache',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leadaccountissue',
            name='comments_cache',
            field=models.TextField(blank=True, null=True),
        ),
    ]
