# Generated by Django 3.1.8 on 2021-06-17 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fds_newsletter", "0001_squashed_0010_auto_20210621_1022"),
        ("fds_donation", "0031_auto_20210111_2055"),
    ]

    operations = [
        migrations.AddField(
            model_name="donor",
            name="subscriber",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fds_newsletter.subscriber",
            ),
        ),
        migrations.AlterField(
            model_name="donor",
            name="salutation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Hello"),
                    ("formal", "Good day"),
                    ("formal_f", "Dear Ms."),
                    ("formal_m", "Dear Mr."),
                    ("informal_f", "Dear"),
                    ("informal_m", "Dear"),
                    ("informal_n", "Dear"),
                ],
                max_length=25,
            ),
        ),
    ]
