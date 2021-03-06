# Generated by Django 2.1.7 on 2019-03-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0233_bundler_slack_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadaccountissue',
            name='issue_type',
            field=models.CharField(choices=[('Ban Account Request', 'Ban Account Request'), ('Connection Issue', 'Connection Issue'), ('Wrong Password', 'Wrong Password'), ('Security Checkpoint', 'Security Checkpoint'), ('Phone Number Change', 'Phone Number Change'), ('Address Change', 'Address Change'), ('Reshipment Needed', 'Reshipment Needed'), ('Missing Payment', 'Missing Payment'), ('Returned Check', 'Returned Check'), ('Charge to Account', 'Charge to Account'), ('Bill Left on Account', 'Bill Left on Account'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='leadaccountissue',
            name='new_value',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='leadaccountissue',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='leadaccountissue',
            name='status',
            field=models.CharField(choices=[('Reported', 'Reported'), ('Submitted', 'Submitted'), ('Rejected', 'Rejected'), ('Reshipped', 'Reshipped'), ('Cancelled', 'Cancelled'), ('Verified', 'Verified'), ('Paid', 'Paid')], default='Reported', max_length=50),
        ),
    ]
