# Generated by Django 3.0.5 on 2020-06-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds_donation', '0023_remove_donor_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationformcmsplugin',
            name='collapsed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='salutation',
            field=models.CharField(blank=True, choices=[('', 'Hallo'), ('formal', 'Good day'), ('formal_f', 'Sehr geehrte Frau'), ('formal_m', 'Sehr geehrter Herr'), ('informal_f', 'Liebe'), ('informal_m', 'Lieber'), ('informal_n', 'Lieber')], max_length=25),
        ),
    ]
