# Generated by Django 2.1.7 on 2019-04-17 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0240_auto_20190410_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadaccountissue',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
