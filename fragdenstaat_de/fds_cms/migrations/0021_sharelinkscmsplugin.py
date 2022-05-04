# Generated by Django 2.2.4 on 2020-02-24 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("fds_cms", "0020_pageannotationcmsplugin_zoom"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShareLinksCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_cms_sharelinkscmsplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
