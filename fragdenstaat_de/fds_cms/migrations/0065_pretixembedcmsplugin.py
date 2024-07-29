# Generated by Django 4.2.14 on 2024-07-29 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0035_auto_20230822_2208_squashed_0036_auto_20240311_1028"),
        (
            "fds_cms",
            "0061_sharelinkscmsplugin_icons_only_and_more_squashed_0064_alter_sharelinkscmsplugin",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="PretixEmbedCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("shop_url", models.TextField()),
                ("js_url", models.TextField()),
            ],
            bases=("cms.cmsplugin",),
        )
    ]
