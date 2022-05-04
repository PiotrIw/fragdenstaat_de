# Generated by Django 3.2.12 on 2022-03-10 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import cms.models.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ("fds_cms", "0044_cardimagecmsplugin_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardcmsplugin",
            name="page_link",
            field=cms.models.fields.PageField(
                blank=True,
                help_text="if present card will be clickable",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cms.page",
                verbose_name="page link",
            ),
        ),
        migrations.AddField(
            model_name="cardcmsplugin",
            name="url",
            field=models.CharField(
                blank=True,
                help_text="if present card will be clickable",
                max_length=255,
                null=True,
                verbose_name="link",
            ),
        ),
        migrations.AddField(
            model_name="cardheadercmsplugin",
            name="background_image",
            field=filer.fields.image.FilerImageField(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.FILER_IMAGE_MODEL,
                verbose_name="Background image",
            ),
        ),
        migrations.AlterField(
            model_name="cardcmsplugin",
            name="shadow",
            field=models.CharField(
                choices=[("no", "No"), ("auto", "Auto"), ("always", "Always")],
                default="no",
                max_length=10,
                verbose_name="Shadow",
            ),
        ),
        migrations.AlterField(
            model_name="cardcmsplugin",
            name="spacing",
            field=models.CharField(
                choices=[("sm", "Small"), ("md", "Medium"), ("lg", "Large")],
                default="md",
                max_length=3,
                verbose_name="Spacing",
            ),
        ),
    ]
