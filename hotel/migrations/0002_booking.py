# Generated by Django 4.1.4 on 2022-12-16 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("days", models.IntegerField(max_length=100)),
                ("amount", models.FloatField()),
                ("food", models.BooleanField(default=False)),
                ("spa", models.BooleanField(default=False)),
                ("gym", models.BooleanField(default=False)),
                ("swimming", models.BooleanField(default=False)),
                ("games", models.BooleanField(default=False)),
                (
                    "bookedBy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel.user"
                    ),
                ),
            ],
        ),
    ]
