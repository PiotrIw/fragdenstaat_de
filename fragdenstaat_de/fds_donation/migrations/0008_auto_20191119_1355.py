# Generated by Django 2.2.4 on 2019-11-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds_donation', '0007_auto_20191114_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donor',
            options={'ordering': ('-last_donation',), 'verbose_name': 'donor', 'verbose_name_plural': 'donors'},
        ),
        migrations.AddField(
            model_name='donationformcmsplugin',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
