# Generated by Django 4.2.16 on 2025-02-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                (
                    "description",
                    models.CharField(
                        help_text="Short description, will be shown in the list view",
                        max_length=255,
                        verbose_name="Description",
                    ),
                ),
                ("start_date", models.DateTimeField(verbose_name="Start")),
                ("end_date", models.DateTimeField(verbose_name="End")),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Location"
                    ),
                ),
            ],
            options={
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
    ]
