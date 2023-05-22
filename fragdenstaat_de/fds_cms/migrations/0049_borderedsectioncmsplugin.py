# Generated by Django 3.2.12 on 2022-06-01 07:58

import django.db.models.deletion
from django.db import migrations, models

import djangocms_frontend.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("fds_cms", "0048_auto_20220601_0923"),
    ]

    operations = [
        migrations.CreateModel(
            name="BorderedSectionCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_cms_borderedsectioncmsplugin",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255)),
                (
                    "border",
                    models.CharField(
                        choices=[
                            ("blue", "Blue"),
                            ("gray", "Gray"),
                            ("yellow", "Yellow"),
                        ],
                        default="gray",
                        max_length=50,
                        verbose_name="Border",
                    ),
                ),
                (
                    "spacing",
                    models.CharField(
                        choices=[("sm", "Small"), ("md", "Medium"), ("lg", "Large")],
                        default="md",
                        max_length=3,
                        verbose_name="Spacing",
                    ),
                ),
                (
                    "heading",
                    models.CharField(
                        choices=[
                            ("h1", "Headline 1"),
                            ("h2", "Headline 2"),
                            ("h3", "Headline 3"),
                            ("h4", "Headline 4"),
                            ("h5", "Headline 5"),
                            ("h6", "Headline 6"),
                        ],
                        default="h3",
                        max_length=5,
                        verbose_name="Heading level",
                    ),
                ),
                (
                    "attributes",
                    djangocms_frontend.fields.AttributesField(
                        blank=True, default=dict, verbose_name="Attributes"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
