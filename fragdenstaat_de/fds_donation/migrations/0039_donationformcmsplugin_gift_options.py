# Generated by Django 4.0.7 on 2022-09-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds_donation', '0038_alter_donation_options_alter_donor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationformcmsplugin',
            name='gift_options',
            field=models.ManyToManyField(blank=True, to='fds_donation.donationgift'),
        ),
    ]
