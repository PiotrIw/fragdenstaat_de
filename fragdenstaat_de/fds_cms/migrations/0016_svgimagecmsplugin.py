# Generated by Django 2.2.4 on 2019-10-17 11:25

import django.db.models.deletion
from django.db import migrations, models

import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("filer", "0011_auto_20190418_0137"),
        ("fds_cms", "0015_vegachartcmsplugin"),
    ]

    operations = [
        migrations.CreateModel(
            name="SVGImageCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_cms_svgimagecmsplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "svg",
                    filer.fields.file.FilerFileField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="filer.File",
                        verbose_name="image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
