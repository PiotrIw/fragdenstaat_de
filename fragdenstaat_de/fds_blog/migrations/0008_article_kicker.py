# Generated by Django 3.2.12 on 2022-07-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds_blog', '0007_articlepreviewplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='kicker',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
