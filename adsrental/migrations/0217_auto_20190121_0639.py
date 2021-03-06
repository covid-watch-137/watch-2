# Generated by Django 2.1.5 on 2019-01-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0216_leadaccount_wrong_password_change_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadaccount',
            name='ban_reason',
            field=models.CharField(blank=True, choices=[('Google - Policy', 'Google - Policy'), ('Google - Billing', 'Google - Billing'), ('Google - Unresponsive User', 'Google - Unresponsive User'), ('Facebook - Policy', 'Facebook - Policy'), ('Facebook - Suspicious', 'Facebook - Suspicious'), ('Facebook - Lockout', 'Facebook - Lockout'), ('Facebook - Unresponsive User', 'Facebook - Unresponsive User'), ('Duplicate', 'Duplicate'), ('Bad ad account', 'Bad ad account'), ('auto_offline', 'Auto: offline for 2 weeks'), ('auto_wrong_password', 'Auto: wrong password for 2 weeks'), ('auto_checkpoint', 'Auto: reported security checkpoint for 2 weeks'), ('auto_not_used', 'Auto: not used for 2 weeks after delivery'), ('ADSDB', 'Banned by Adsdb sync'), ('Quit', 'Quit'), ('Other', 'Other')], help_text='Populated from ban form', max_length=50, null=True),
        ),
    ]
